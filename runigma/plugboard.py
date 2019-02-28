# Copyright (C) 2016-2019 by Vd.
# Copyright (C) 2012 by Brian Neal.
# This file is part of RuNigma, the RuNigma Machine.
# RuNigma is released under the MIT License (see LICENSE).

"""Contains the Plugboard class for simulating the plugboard
component of the RuNigma Machine.

"""

import collections
import copy
from itertools import chain
import string


# On Heer & Luftwaffe (?) models, the plugs are labeled with upper case letters
HEER_LABELS = 'abcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789_'
HEER_LABELS_LEN = len(HEER_LABELS)

# The number of plugboard cables supplied with a machine:
MAX_PAIRS = 20


class PlugboardError(Exception):
    pass


class Plugboard:
    """The plugboard allows the operator to swap letters before and after the 
    entry wheel. This is accomplished by connecting cables between pairs of
    plugs that are marked with letters (Heer & Luftwaffe models) or numbers
    (Kriegsmarine). Ten cables were issued with each machine; thus up to 10 of
    these swappings could be used as part of a machine setup.

    Each cable swaps both the input and output signals. Thus if A is connected
    to B, A crosses to B in the keyboard to entry wheel direction and also in
    the reverse entry wheel to lamp direction.

    """
    def __init__(self, wiring_pairs=None):
        """Configure the plugboard according to a list or tuple of integer
        pairs, or None.

        A value of None or an empty list/tuple indicates no plugboard
        connections are to be used (i.e. a straight mapping).

        Otherwise wiring_pairs must be an iterable of integer pairs, where each
        integer is between 0-25, inclusive. At most 10 such pairs can be
        specified. Each value represents an input/output path through the
        plugboard. It is invalid to specify the same path more than once in the
        list.

        If an invalid wiring_pairs parameter is given, a PlugboardError is
        raised.

        """
        # construct wiring mapping table with default 1-1 mappings
        self.wiring_map = list(range(HEER_LABELS_LEN))

        # construct backup storage for the wiring map; this is useful when
        # hill-climbing and is used when the Plugboard is used as a context
        # manager
        self._backup_map = list(range(HEER_LABELS_LEN))

        # use settings if provided
        if not wiring_pairs:
            return

        if len(wiring_pairs) > MAX_PAIRS:
            raise PlugboardError('Please specify %d or less pairs' % MAX_PAIRS)

        # ensure a path occurs at most once in the list
        counter = collections.Counter(chain.from_iterable(wiring_pairs))
        path, count = counter.most_common(1)[0]
        if count != 1:
            raise PlugboardError('duplicate connection: %d' % path)

        # make the connections
        for pair in wiring_pairs:
            m = pair[0]
            n = pair[1]
            if not (0 <= m < HEER_LABELS_LEN) or not (0 <= n < HEER_LABELS_LEN):
                raise PlugboardError('invalid connection: %s' % str(pair))

            self.wiring_map[m] = n
            self.wiring_map[n] = m

    @classmethod
    def from_key_sheet(cls, settings=None):
        """Configure the plugboard according to a settings string as you may
        find on a key sheet.

        Two syntaxes are supported, the Heer/Luftwaffe and Kriegsmarine styles:

        In the Heer syntax, the settings are given as a string of
        alphabetic pairs. For example: 'PO ML IU KJ NH YT GB VF RE DC'

        To specify no plugboard connections, settings can be None or an empty
        string.

        A PlugboardError will be raised if the settings string is invalid, or if
        it contains more than MAX_PAIRS pairs. Each plug should be present at
        most once in the settings string.

        """
        if not settings:
            return cls(None)

        wiring_pairs = []

        pairs = settings.split()

        for p in pairs:
            if len(p) != 2:
                raise PlugboardError('invalid pair: %s' % p)

            m = p[0]
            n = p[1]
            if m not in HEER_LABELS or n not in HEER_LABELS:
                raise PlugboardError('invalid pair: %s' % p)

            wiring_pairs.append((HEER_LABELS.index(m), HEER_LABELS.index(n)))

        return cls(wiring_pairs)

    def get_pairs(self):
        """Return the connections as a set of tuple pairs."""
        pairs = set()
        for x in range(0, HEER_LABELS_LEN):
            y = self.wiring_map[x]
            if x != y and (y, x) not in pairs:
                pairs.add((x, y))

        return pairs

    def army_str(self):
        """Return settings as a string as found on an army key sheet."""
        pairs = list(self.get_pairs())
        pairs.sort()
        return ' '.join('{}{}'.format(chr(t[0] + ord('A')), 
                                      chr(t[1] + ord('A'))) for t in pairs)

    def __str__(self):
        """Returns a string representation of the settings in army format."""
        return self.army_str()

    def signal(self, n):
        """Simulate a signal entering the plugboard on wire n, where n must be
        an integer between 0 and 25.

        Returns the wire number of the output signal (0-25).

        Note that since the plugboard always crosses pairs of wires, it doesn't
        matter what direction (keyboard -> entry wheel or vice versa) the signal
        is coming from.

        """

        return self.wiring_map[n]

    # Support for hill-climbing algorithms:

    def get_wiring(self):
        """Returns a deep copy of the internal wiring map."""
        return copy.deepcopy(self.wiring_map)

    def is_wired(self, n):
        """Returns True if connection n has a cable attached; 0 <= n < 70."""
        return self.wiring_map[n] != n

    def is_free(self, n):
        """Returns True if connection n has no cable attached; 0 <= n < 70."""
        return self.wiring_map[n] == n

    def __enter__(self):
        """Saves the current state of the wiring map."""
        for n in range(HEER_LABELS_LEN):
            self._backup_map[n] = self.wiring_map[n]
        return self

    def __exit__(self, *exc_info):
        """Restores the saved state of the wiring map."""
        for n in range(HEER_LABELS_LEN):
            self.wiring_map[n] = self._backup_map[n]

    def connection(self, n):
        """Returns plug number [0-25] for what is connected to plug n [0-25]."""
        return self.wiring_map[n]

    def disconnect(self, n):
        """Removes cable from plug number n [0-25]."""
        x = self.wiring_map[n]
        self.wiring_map[x] = x
        self.wiring_map[n] = n

    def connect(self, x, y):
        """Connects plug x to plug y, removing any existing connections first.
        
        x and y must be in [0-25].

        """
        # disconnect any existing connections
        m = self.wiring_map[x]
        n = self.wiring_map[y]
        self.wiring_map[m] = m
        self.wiring_map[n] = n

        self.wiring_map[x] = y
        self.wiring_map[y] = x

    def is_connected(self, x, y):
        """Returns True if x is connected to y.

        x and y must be in [0-25].

        """
        return self.wiring_map[x] == y and self.wiring_map[y] == x


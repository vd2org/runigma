# Copyright (C) 2016-2019 by Vd.
# Copyright (C) 2012 by Brian Neal.
# This file is part of RuNigma, the RuNigma Machine.
# RuNigma is released under the MIT License (see LICENSE).

"""This module contains the top-level RuNigmaMachine class for the RuNigma Machine
simulation.

"""
import string

from .rotors.factory import create_rotor, create_reflector
from .plugboard import Plugboard
from .keyfile import get_daily_settings


class RuNigmaError(Exception):
    pass

# The RuNigma keyboard consists of the 70 letters of the alphabet, uppercase
# only:
KEYBOARD_CHARS = 'abcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789_'
KEYBOARD_CHARS_LEN = len(KEYBOARD_CHARS)
KEYBOARD_SET = set(KEYBOARD_CHARS)


class RuNigmaMachine:
    """Top-level class for the RuNigma Machine."""

    def __init__(self, rotors, reflector, plugboard):
        """Configures the RuNigma Machine. Parameters are as follows:

        rotors - a list containing 5 Rotor objects. The order of the list
        is important. The first rotor is the left-most rotor, and the last
        rotor is the right-most (from the operator's perspective sitting at
        the machine).

        reflector - a rotor object to represent the reflector

        plugboard - a plugboard object to represent the state of the plugboard

        """
        if len(rotors) != 5:
            raise RuNigmaError("Must supply 5 rotors")

        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard

    @classmethod
    def from_key_sheet(cls, rotors='А Б В Г Д', ring_settings=None,
            reflector='А', plugboard_settings=None):

        """Convenience function to build an RuNigmaMachine from the data as you
        might find it on a key sheet:

        rotors: either a list of strings naming the rotors from left to right
        or a single string:
            e.g. ["A", "Б", "В", "Г", "Д"] or "А Б В Г Д"

        ring_settings: either a list/tuple of integers, a string, or None to
        represent the ring settings to be applied to the rotors in the rotors
        list. The acceptable values are:
            - A list/tuple of letters with values between A-_
            - A string; either space separated letters, e.g. 'А Б В Г Д'.
            - None means all ring settings are "a".

        reflector: a string that names the reflector to use

        plugboard_settings: a string of plugboard settings as you might find
        on a key sheet; e.g. 'АБ ВГ ЕЖ ЗИ КЛ МН ОП РС ТУ ФХ'. A value of None means
        no plugboard connections are made.

        """
        # validate inputs
        if isinstance(rotors, str):
            rotors = rotors.split()

        if len(rotors) != 5:
            raise RuNigmaError("invalid rotors list size")

        if ring_settings is None:
            ring_settings = [0] * 5
        else:
            strings = ring_settings.split()
            ring_settings = []
            for s in strings:
                ring_settings.append(KEYBOARD_CHARS.index(s))

        if len(ring_settings) != 5:
            raise RuNigmaError("invalid ring list size")

        # assemble the machine
        rotor_list = [create_rotor(r[0], r[1]) for r in zip(rotors, ring_settings)]

        return cls(rotor_list, 
                   create_reflector(reflector),
                   Plugboard.from_key_sheet(plugboard_settings))

    @classmethod
    def from_key_file(cls, fp, day=None):
        """Convenience function to read key parameters from a file.

        fp - a file-like object that contains daily key settings
        day - the line labeled with the day number (1-366) will be used for the
        settings. If day is None, the day number will be determined from today's
        date. 

        For more information on the file format, see keyfile.py.

        """
        args = get_daily_settings(fp, day)
        return cls.from_key_sheet(**args)

    def set_display(self, val):
        """Sets the rotor operator windows to 'val'.

        'val' must be a string or iterable containing values for each window
        from left to right.

        """
        if len(val) != 5:
            raise RuNigmaError("Incorrect length for display value")

        for i, rotor in enumerate(reversed(self.rotors)):
            rotor.set_display(val[-1 - i])

    def get_display(self):
        """Returns the operator display as a string."""
        
        return ''.join([r.get_display() for r in self.rotors])

    def key_press(self, key):
        """Simulate a front panel key press. 

        key - a string representing the letter pressed

        The rotors are stepped by simulating the mechanical action of the
        machine. 
        Next a simulated current is run through the machine.
        The lamp that is lit by this key press is returned as a string.

        """
        if key not in KEYBOARD_SET:
            raise RuNigmaError('illegal key press %s' % key)

        # simulate the mechanical action of the machine
        self._step_rotors()

        # simulate the electrical operations:
        signal_num = KEYBOARD_CHARS.index(key)
        lamp_num = self._electric_signal(signal_num)
        return KEYBOARD_CHARS[lamp_num]

    def _step_rotors(self):
        """Simulate the mechanical action of pressing a key."""
        
        # The right-most rotor's right-side ratchet is always over a pawl, and
        # it has no neighbor to the right, so it always rotates.
        #
        # The middle rotors will rotate if either:
        #   1) The right rotor's left side notch is over the 2nd pawl
        #       or
        #   2) It has a left-side notch over the 3rd pawl
        #
        # The fifth rotor (from the right) will rotate only if the fourth rotor
        # has a left-side notch over the 3rd pawl.

        rotor1 = self.rotors[-1]
        rotor2 = self.rotors[-2]
        rotor3 = self.rotors[-3]
        rotor4 = self.rotors[-4]
        rotor5 = self.rotors[-5]

        # decide which rotors can move
        rotate2 = rotor1.notch_over_pawl() or rotor2.notch_over_pawl()
        rotate3 = rotor2.notch_over_pawl() or rotor3.notch_over_pawl()
        rotate4 = rotor3.notch_over_pawl() or rotor4.notch_over_pawl()
        rotate5 = rotor4.notch_over_pawl() or rotor5.notch_over_pawl()

        # move rotors
        rotor1.rotate()
        if rotate2:
            rotor2.rotate()
        if rotate3:
            rotor3.rotate()
        if rotate4:
            rotor4.rotate()
        if rotate5:
            rotor5.rotate()

    def _electric_signal(self, signal_num):
        """Simulate running an electric signal through the machine in order to
        perform an encrypt or decrypt operation

        signal_num - the wire (0-69) that the simulated current occurs on

        Returns a lamp number to light (an integer 0-69).

        """
        pos = self.plugboard.signal(signal_num)

        for rotor in reversed(self.rotors):
            pos = rotor.signal_in(pos)

        pos, plaintext = self.reflector.signal_in_reflector(pos)
        
        if plaintext:
            return signal_num

        for rotor in self.rotors:
            pos = rotor.signal_out(pos)

        return self.plugboard.signal(pos)

    def process_text(self, text, replace_char='_'):
        """Run the text through the machine, simulating a key press for each
        letter in the text.

        text - the text to process. Note that the text is converted to upper
        case before processing.

        replace_char - if text contains a character not on the keyboard, replace
        it with replace_char; if replace_char is None the character is dropped
        from the message

        """
        result = []
        for key in text:
            if key not in KEYBOARD_SET: 
                if replace_char:
                    key = replace_char
                else:
                    continue    # ignore it

            result.append(self.key_press(key))

        return ''.join(result)

    def get_rotor_counts(self):
        """Return the rotor rotation counts as a list of integers."""
        return [r.rotations for r in self.rotors]

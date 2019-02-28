# Copyright (C) 2016-2019 by Vd.
# This file is part of RuNigma, the RuNigma Machine.
# RuNigma is released under the MIT License (see LICENSE).

"""Provide RuNigma key sheet generator.

"""
import argparse
from random import choice

from runigma.machine import KEYBOARD_CHARS
from runigma.rotors.data import ROTORS, REFLECTORS

SHEET_HEADER = "#   Day     Rotors      Rings       Plugboard" \
               "                                                       Reflector"
SHEET_STR = "    %3d    %s  %s  %s     %s"

PROG_DESC = 'Generates key sheets for RuNigma.'

HELP_EPILOG = """\
You can generate standard 366-days sheet.

Usage:

    $ %(prog)s > keysheet.txt

"""


def main():
    parser = argparse.ArgumentParser(prog='runigma', description=PROG_DESC, epilog=HELP_EPILOG,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-d', '--days', type=int, default=366,
                        help='number of days to generate')

    args = parser.parse_args()
    print(SHEET_HEADER)
    for day in range(args.days):
        rotors = ''
        rings = ''
        reflector = choice(list(REFLECTORS.keys()))
        plugboard = ''

        # generate rotors:
        rtrs = list(ROTORS.keys())
        for i in range(5):
            r = choice(rtrs)
            rtrs.remove(r)
            rotors += ' %s' % r

        # generate rings:
        for i in range(5):
            rings += ' %s' % choice(KEYBOARD_CHARS)

        # generate plugboard:
        chrs = list(KEYBOARD_CHARS)
        for i in range(20):
            la = choice(chrs)
            chrs.remove(la)
            lb = choice(chrs)
            chrs.remove(lb)
            plugboard += ' %s%s' % (la, lb)

        print(SHEET_STR % (day + 1, rotors, rings, plugboard, reflector))


if __name__ == '__main__':
    main()

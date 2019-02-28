# Copyright (C) 2016-2019 by Vd.
# Copyright (C) 2012 by Brian Neal.
# This file is part of RuNigma, the RuNigma Machine.
# RuNigma is released under the MIT License (see LICENSE).

"""Provide an example command-line app that can setup an RuNigmaMachine and
process text.

"""

import argparse
import sys

from .keyfile import KeyFileError
from .machine import RuNigmaMachine, RuNigmaError
from .rotors import RotorError

PROG_DESC = 'Encrypt/decrypt text according to RuNigma machine key settings'

HELP_EPILOG = """\
Key settings can either be specified by command-line arguments, or read
from a key file. If reading from a key file, the line labeled with the
current day number is used unless the --day argument is provided.

Text to process can be supplied 3 ways:

   if --text=TEXT is present TEXT is processed
   if --file=FILE is present the contents of FILE are processed
   otherwise the text is read from standard input

Examples:

    $ %(prog)s --key-file=enigma.keys -s ФСИАР -t HELLOXWORLDX
    $ %(prog)s -r A Б В Г Д -i 1 2 3 4 5 -p AB CD EF GH IJ KL MN -u Ф -s АУГСД
  
"""


def create_from_key_file(filename, day=None):
    """Create an RuNigmaMachine from a daily key sheet."""

    with open(filename, 'r') as f:
        return RuNigmaMachine.from_key_file(f, day)


def create_from_args(parser, args):
    """Create an RuNigmaMachine from command-line specs."""

    if args.rotors is None:
        parser.error("Please specify 5 rotors; e.g. А Б В Г Д")
    elif len(args.rotors) != 5:
        parser.error("Expecting 5 rotors; %d supplied" % len(args.rotors))

    if args.text and args.file:
        parser.error("Please specify --text or --file, but not both")

    ring_settings = ' '.join(args.ring_settings) if args.ring_settings else None
    plugboard = ' '.join(args.plugboard) if args.plugboard else None

    return RuNigmaMachine.from_key_sheet(rotors=args.rotors,
                                         ring_settings=ring_settings,
                                         plugboard_settings=plugboard,
                                         reflector=args.reflector)


def main():
    parser = argparse.ArgumentParser(prog='runigma', description=PROG_DESC, epilog=HELP_EPILOG,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-k', '--key-file',
                        help='path to key file for daily settings')
    parser.add_argument('-d', '--day', type=int, default=None,
                        help='use the settings for day DAY when reading key file')
    parser.add_argument('-r', '--rotors', nargs='+', metavar='ROTOR',
                        help='rotor list ordered from left to right; e.g А Б В Г Д')
    parser.add_argument('-i', '--ring-settings', nargs='+',
                        metavar='RING_SETTING',
                        help='ring setting list from left to right; e.g. А А Г Д У')
    parser.add_argument('-p', '--plugboard', nargs='+', metavar='PLUGBOARD',
                        help='plugboard settings')
    parser.add_argument('-u', '--reflector', help='reflector name')
    parser.add_argument('-s', '--start', help='starting position')
    parser.add_argument('-t', '--text', help='text to process')
    parser.add_argument('-f', '--file', help='input file to process')
    parser.add_argument('-x', '--replace-char', default='_',
                        help=('if the input text contains chars not found on the enigma'
                              ' keyboard, replace with this char [default: %(default)]'))
    parser.add_argument('-z', '--delete-chars', default=False,
                        action='store_true',
                        help=('if the input text contains chars not found on the enigma'
                              ' keyboard, delete them from the input'))
    parser.add_argument('-v', '--verbose', action='store_true', default=False,
                        help='provide verbose output; include final rotor positions')

    args = parser.parse_args()

    if args.key_file and (args.rotors or args.ring_settings or args.plugboard
                          or args.reflector):
        parser.error("Please specify either a key file or command-line key "
                     "settings, but not both")

    if args.start is None:
        parser.error("Please specify a start position")

    if args.key_file:
        machine = create_from_key_file(args.key_file, args.day)
    else:
        machine = create_from_args(parser, args)

    if args.text:
        text = args.text
    elif args.file:
        with open(args.file, 'r') as f:
            text = f.read()
    else:
        text = input('--> ')

    replace_char = args.replace_char if not args.delete_chars else None

    machine.set_display(args.start)

    s = machine.process_text(text, replace_char=replace_char)

    if args.verbose:
        print('Final rotor positions:', machine.get_display())
        print('Rotor rotation counts:', machine.get_rotor_counts())
        print('Output:')

    print(s)


def console_main():
    try:
        main()
    except (IOError, RuNigmaError, RotorError, KeyFileError) as ex:
        sys.stderr.write("%s\n" % ex)


if __name__ == '__main__':
    console_main()

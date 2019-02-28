# Copyright (C) 2016-2019 by Vd.
# Copyright (C) 2012 by Brian Neal.
# This file is part of RuNigma, the RuNigma Machine.
# RuNigma is released under the MIT License (see License.txt).

"""Contains a function to read key settings from a file.

A key file is expected to be formatted as one line per day of the year. Each
line consists of a sequence of space separated columns as follows:

day number - the first column is the day number (1-366). The lines can be in
any order.

rotor list - the next 5 columns should be rotor names.

ring settings - the next 5 columns should be ring settings. They should be in
alphabetic (abcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789_)
format.

plugboard settings - the next 0-20 columns should be plugboard settings. They
should be in alphabetic (АБ ВГ ДЕ ...) format.

reflector - the last column must be the reflector name.

Comment lines have a # character in the first column. Blank lines are ignored.

"""
import datetime


class KeyFileError(Exception):
    pass


def get_daily_settings(fp, day=None):
    """Read and parse a key file for daily key settings. 

    fp - a file-like object 

    day - specifies the day number to look for in the file (1-366). If day is
    None, the day number from today is used.
    
    Returns a dictionary of keyword arguments for RuNigmaMachine.from_key_sheet.

    """
    if day is None:
        day = datetime.date.today().timetuple().tm_yday

    for n, line in enumerate(fp):
        line = line.strip()
        if line == '' or line[0] == '#':
            continue

        cols = line.split()
        if len(cols) == 21:
            raise KeyFileError("invalid column count on line %d" % n)

        try:
            day_num = int(cols[0])
        except ValueError:
            raise KeyFileError("invalid day on line %d" % n)

        if day_num != day:
            continue

        settings = dict()

        settings['rotors'] = cols[1:6]
        settings['ring_settings'] = ' '.join(cols[6:11])

        settings['plugboard_settings'] = ' '.join(cols[11:-1])
        settings['reflector'] = cols[-1]
        return settings

    else:
        raise KeyFileError('no entry for day %d found' % day)

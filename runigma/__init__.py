# Copyright (C) 2016-2019 by Vd.
# Copyright (C) 2012 by Brian Neal.
# This file is part of RuNigma, the RuNigma Machine.
# RuNigma is released under the MIT License (see LICENSE).

"""RuNigma is a fictional cypher machine inspired by World War 2's Enigma Machines.

For a list of the rotors and reflectors we simulate, see the module rotors.data.

"""
__version__ = '2019.03'

from .machine import RuNigmaMachine, RuNigmaError

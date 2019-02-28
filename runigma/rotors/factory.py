# Copyright (C) 2016-2019 by Vd.
# Copyright (C) 2012 by Brian Neal.
# This file is part of RuNigma, the RuNigma Machine.
# RuNigma is released under the MIT License (see LICENSE).

"""Contains factory functions for creating rotors and reflectors."""

from . import RotorError
from .rotor import Rotor
from .data import ROTORS, REFLECTORS


def create_rotor(model, ring_setting=0):
    """Factory function to create and return a rotor of the given model name."""

    if model in ROTORS:
        data = ROTORS[model]
        return Rotor(model, data['wiring'], ring_setting, data['stepping'])

    raise RotorError("Unknown rotor type: %s" % model)


def create_reflector(model):
    """Factory function to create and return a reflector of the given model
    name.
    
    """
    if model in REFLECTORS:
        return Rotor(model, wiring=REFLECTORS[model]['wiring'], plaintext=REFLECTORS[model]['plaintext'])

    raise RotorError("Unknown reflector type: %s" % model)

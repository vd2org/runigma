# Copyright (C) 2016-2019 by Vd.
# Copyright (C) 2012 by Brian Neal.
# This file is part of RuNigma, the RuNigma Machine.
# RuNigma is released under the MIT License (see LICENSE).

import setuptools
from os.path import join, dirname

import runigma

setuptools.setup(
    name='runigma',
    version=runigma.__version__,
    author='Vd',
    author_email='vd@vd2.org',
    url='https://github.com/vd2org/runigma',
    license='MIT',
    description='RuNigma is a fictional cypher machine inspired by World War 2''s Enigma Machines.',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    packages=['runigma', 'runigma.rotors', 'runigma.tests'],
    scripts=['runigma/bin/runigma', 'runigma/bin/runigma-sheet'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Communications',
        'Topic :: Security',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)

# Copyright (C) 2016-2019 by Vd.
# Copyright (C) 2012 by Brian Neal.
# This file is part of RuNigma, the RuNigma Machine.
# RuNigma is released under the MIT License (see License.txt).

from distutils.core import setup
from os.path import join, dirname

import runigma

setup(
    name='py-enigma',
    version=runigma.__version__,
    author='Vd',
    author_email='vd@vd2.org',
    url='https://github.com/vd2org/runigma',
    license='MIT',
    description='A historically accurate Enigma machine simulation library.',
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    packages=['runigma', 'runigma.rotors', 'runigma.tests'],
    package_data=dict(enigma=['examples/*.py',
                              'docs/source/*.rst',
                              'docs/source/*.py',
                             ]),
    scripts=['runigma.py'],
    classifiers = [
        'Development Status :: 3 - Alpha',
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

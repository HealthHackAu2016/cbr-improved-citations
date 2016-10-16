#!/usr/bin/env python3
"""
Metadata and setup info for installation.

See  https://packaging.python.org/en/latest/distributing.html
"""

import setuptools

with open('README.rst') as f:
    long_description = f.read()
with open('VERSION.txt') as f:
    version = f.read().strip()

config = dict(
    name='CITeX',
    version=version,
    description='Tools to manage large BibTex libraries',
    long_description=long_description,

    author='Aqeel Akber, Michael Barson, Sam Blackwell, Zac Hatfield-Dodds',
    author_email='zac.hatfield.dodds@gmail.com',
    license='GPL3+',
    url='https://github.com/HealthHackAu2016/cbr-improved-citations',

    keywords='endnote bibtex latex duplicates filter cite citation reference',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering',
    ],

    packages=['.'],
    install_requires=['pybtex', 'unidecode'],
    extras_require={},
    entry_points={'console_scripts': ['citex=dedupe:console']},
)

if __name__ == '__main__':
    setuptools.setup(**config)

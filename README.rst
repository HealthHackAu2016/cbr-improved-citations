CITeX - 'Big Citations' tooling
###############################

CITeX is a set of tools for comparing and filtering very large reference databases.

Description
===========

CITeX searches through BibTeX files to search and remove duplicate entries.  It does this by comparing parsed titles strings and for simple cases, it then groups by similarities computes scores and selects the best single citation from that group of duplicates.

This project was a part of HealthHack 2016 in Canberra.

**Problem owner**: Andrea Parisi

**Hackers**: Aqeel Akber, Michael Barson, Sam Blackwell, Zac Hatfield-Dodds

.. image:: citex.png
   :width: 250px
   :align: center

Installation
============

CITeX is on PyPI, use ``python -m pip install --upgrade citex`` to install or update.
If you do not have Python, download the latest version from https://python.org


Usage
=====
Open a command prompt in the directory with your Bibtex files (see below).

Run the ``citex`` or ``citex-check`` command followed by the files to process.

See ``citex --help`` for details

For any number (one or more) of input files (collectively L) CITex outputs three files:  

- dedupe - the best selection of the duplicates (B)
- dupes - the remaining duplicates (R)
- unique - originial unique citations (U)


BibTex files
============

For Endnote users BibTeX files can be exported.

In Endnote:

- Go to the ``Edit > Output Styles > Style Manager`` menu
- select 'BibTex export'
- close Style Manager
- select all items (ctrl-a)
- `File > Export`
- save file

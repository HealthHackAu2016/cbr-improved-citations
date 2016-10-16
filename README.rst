CITeX - 'Big Citations' tooling
###############################

CITeX is a set of tools for comparing and filtering very large reference databases.

Description
===========

CITeX searches through BibTeX files to search and remove duplicate entries.  It does this by comparing parsed titles strings and for simple cases, it then groups by similarities computes scores and selects the best single citation from that group of duplicates.

This project was a part of HealthHack 2016 in Canberra.

**Authors**: Aqeel Akber, Michael Barson, Sam Blackwell, Zac Hatfield-Dodds, Andrea Parisi

.. image:: citex.png
   :width: 250px
   :align: center	

Installation
============

CITeX is on PyPI, use ``pip -m install citex`` to install.


Usage
=====

``citex input files``

See ``citex --help`` for details

For a single input file (L) CITex outputs three files:  

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

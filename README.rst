CiTeX - 'Big Citations' tooling
###############################

CiTeX is a set of tools for managing very large reference databases.

Description
===========

CiTeX searches through BibTeX files to search and remove duplicate entries.  It does this by comparing parsed titles strings and for simple cases, it then groups by similarities computes scores and selects the best single citation from that group of duplicates.

This project was a part of HealthHack 2016 in Canberra.

**Authors**: Aqeel Akber, Michael Barson, Sam Blackwell, Zac Hatfield-Dodds

Installation
============
CiTeX is on PyPI, ``pip -m install citex`` to install.


Tools
=====

:export:
        Export from Endnote to BibTex with JabRef (external)
:dedupe:
        Deduplicate BibTex files, including close matches

		
BibTex files
============

For Endnote users BibTeX files can be exported.

In Endnote:

- Go to the ``Edit > Output Styles > Style Manager`` menu
- select 'BibTex export'
- select all items (ctrl-a)
- `File > Export`
- save file

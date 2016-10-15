#! python3
"""
Simple IO functions to get pybtex.database.Entry objects out of and into
files or strings.
"""

import os

from pybtex import database


def read_bib_entries(*locations):
    """Yield pybtex.database.Entry objects from each location in turn.
    Locations can be file names or strings containing file contents.
    """
    for loc in locations:
        if os.path.isfile(loc):
            with open(loc, encoding='latin1') as f:
                loc = f.read()
        yield from database.parse_string(
            loc.replace('}.' ,'},'), 'bibtex').entries.values()


def write_bib_entries(entries, fname=None):
    """Take an iterable of pybtex.database.Entry objects, and return a string.
    If fname is not None, write the string to a file before returning it.
    """
    entries_dict = {e.key: e for e in entries}
    #assert len(entries) == len(entries_dict), 'Entries must have unique keys'
    btex_str = database.BibliographyData(
        entries=entries_dict).to_string('bibtex')
    if fname is not None:
        with open(fname, 'w', encoding='latin1') as f:
            f.write(btex_str)
    return btex_str

#! python3

import collections
import itertools
import sys

import btx_io, choose_best, compare


def group_entries(entries):
    """Takes an iterable of entries, and returns list of lists, where all
    potentially-duplicated entries should be in the same sublist.
    """
    def key_func(entry):
        """Return a key for the group this entry falls into."""
        try:
            year = int(entry.fields.get('year'))
        except:
            year = None
        try:
            return year, int(entry.fields.get('number'))
        except:
            return year, None

    grouper = collections.defaultdict(list)
    for e in entries:
        grouper[key_func(e)].append(e)
    return sorted(grouper.values(), key=len)


def main(*filenames):
    """Do the things."""
    out = []
    for i, grp in enumerate(
            group_entries(btx_io.read_bib_entries(*filenames))):
        as_list_list = compare.compare(grp)
        out.extend(map(choose_best.best_entry, as_list_list))
    btx_io.write_bib_entries(out, fname='test_out.bib')


if __name__ == '__main__':
    # TODO:  use argparse for CLI
    main(sys.argv[1])

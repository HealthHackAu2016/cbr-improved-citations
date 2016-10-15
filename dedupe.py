#! python3
import collections
import itertools
import sys

import btx_io, choose_best, compare


def key_func(entry):
    """Return a key for the group this entry falls into."""
    try:
        year = int(entry.fields.get('year'))
    except:
        year = -1
    try:
        return year, int(entry.fields.get('number'))
    except:
        return year, -1


def group_entries(entries):
    """Takes an iterable of entries, and returns list of lists, where all
    potentially-duplicated entries should be in the same sublist.
    """
    grouper = collections.defaultdict(list)
    for e in entries:
        grouper[key_func(e)].append(e)
    return sorted(grouper.values(), key=len, reverse=True)


def main(*filenames):
    """Do the things."""
    out = []
    inp = list(btx_io.read_bib_entries(*filenames))
    len_in = len(inp)
    for i, grp in enumerate(group_entries(inp)):
        #print(len(grp))
        as_list_list = compare.compare(grp)
        #print(len(as_list_list))
        out.extend(map(choose_best.best_entry, as_list_list))
        if i > 1000:
            break
    print(len_in, len(out))
    btx_io.write_bib_entries(sorted(out, key=key_func), fname='test_out.bib')


if __name__ == '__main__':
    # TODO:  use argparse for CLI
    main(sys.argv[1])

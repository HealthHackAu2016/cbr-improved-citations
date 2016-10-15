#! python3
import collections
import itertools
import os
import sys

import btx_io, choose_best, compare


def title_key(entry):
    return compare.compress_str(entry.fields.get('title', ''))


def dump_titles(*filenames):
    """Do the things."""
    with open('titles.txt', 'w', encoding='latin1') as f:
        out = sorted(compare.compress_str(e.fields.get('title', '')) for e in
                     btx_io.read_bib_entries(*filenames))
        f.write('\n'.join(out))


def main(filenames):
    """Do the things."""
    grouped = collections.defaultdict(list)
    in_ = list(btx_io.read_bib_entries(*filenames))
    for e in in_:
        grouped[title_key(e)].append(e)

    out = ((g[0] if len(g) == 1 else None, g[0] if len(g) > 1 else None,
            g[1:]) for g in grouped.values())
    uniq, dd, dus = zip(*out)
    dus = itertools.chain.from_iterable(dus)
    for group, name in zip((uniq, dd, dus), ('unique_', 'dedupe_', 'dupes_')):
        group = sorted((i for i in group if i is not None), key=title_key)
        if group:
            print('{} {} references of {}'.format(len(group), name, len(in_)))
            btx_io.write_bib_entries(sorted(group, key=title_key),
                                     fname=name + os.path.basename(
                filenames[0]).replace('.txt', '.bib'))


if __name__ == '__main__':
    # TODO:  use argparse for CLI
    main(sys.argv[1:])

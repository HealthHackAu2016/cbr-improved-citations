#! python3
import collections
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


def main(*filenames):
    """Do the things."""
    grouped = collections.defaultdict(list)
    in_ = list(btx_io.read_bib_entries(*filenames))
    for e in in_:
        grouped[title_key(e)].append(e)
    out = sorted([choose_best.best_entry(g)
                  for g in grouped.values()], key=title_key)
    print(len(in_), len(out))
    btx_io.write_bib_entries(out, fname='dedup_' + os.path.basename(
        filenames[0]).replace('.txt', '.bib'))

    return(out)
    
'''
if __name__ == '__main__':
    # TODO:  use argparse for CLI
    main(sys.argv[1])
'''
#! python3
"""
A tool to sort Bibtex references, and split them into a file each for unique
references, the best of each set of duplicate references, and the remaining
duplicates (so that no references are ever lost).
"""
import argparse
import collections
import itertools
import os

import btx_io, choose_best, compare


def title_key(entry):
    return compare.compress_str(entry.fields.get('title', ''))


def dump_titles(*filenames):
    """Do the things."""
    with open('titles.txt', 'w', encoding='latin1') as f:
        out = sorted(compare.compress_str(e.fields.get('title', '')) for e in
                     btx_io.read_bib_entries(*filenames))
        f.write('\n'.join(out))


def main(filenames, out_dir, silent=False):
    """Do the things."""
    grouped = collections.defaultdict(list)
    in_ = list(btx_io.read_bib_entries(*filenames))
    for e in in_:
        grouped[title_key(e)].append(e)

    out = ((g[0] if len(g) == 1 else None, g[0] if len(g) > 1 else None, g[1:])
           for g in (choose_best.sorted_entries(g) for g in grouped.values()))
    uniq, dd, dus = zip(*out)
    uniq = sorted((i for i in uniq if i is not None), key=title_key)
    dd = sorted((i for i in dd if i is not None), key=title_key)
    dus = list(itertools.chain.from_iterable(dus))
    def write(group, tag):
        if not group:
            return
        os.makedirs(out_dir, exist_ok=True)
        fname = os.path.basename(filenames[0]).replace('.txt', '.bib')
        btx_io.write_bib_entries(sorted(group, key=title_key),
                                 fname=os.path.join(out_dir, tag + fname))

    # Now go through, printing descriptions and writing files out.
    if not silent:
        print('There are {} references in the input {}'.format(
              len(in_), 'files' if len(filenames) > 1 else 'file'))
        print('{} articles had no duplicate references'.format(len(uniq)))
        print('{} articles had duplicate references'.format(len(dd)))
        print('There were {} duplicate references in total'.format(
              len(dd) + len(dus)))
        print('The output contains {} unique references'.format(
              len(uniq) + len(dd)))
        print('That means we filtered out {:.1f}% of the library!'.format(
              100 * len(dus) / len(in_)))
    write(uniq, 'unique_')
    write(dd, 'dedupe_')
    write(dus, 'dupes_')

def get_args():
    with open('VERSION.txt') as f:
        version = f.read().strip()
    parser = argparse.ArgumentParser(description=__doc__.strip())
    parser.add_argument('-V', '--version', action='version', version=version)
    parser.add_argument('files', type=str, nargs='+',
                        help='the filenames to process')
    parser.add_argument('-o', '--output-dir', default='out', metavar='DIR',
                        help='directory for output files.  default "./out/"')
    parser.add_argument('--silent', action='store_true',
                        help='do not print statistics')
    return parser.parse_args()


def console():
    args = get_args()
    main(args.files, args.output_dir)


if __name__ == '__main__':
    console()

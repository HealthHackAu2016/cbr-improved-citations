#! python
"""
Companion tool to citex, which heuristically matches close title names.
The output is a single .bib file, with all references in the inputs grouped
and annotated if they may be duplicates.  It is suggested to use this on the
output of citex.
"""
import argparse
import collections
import difflib
import os

import btx_io, compare, dedupe


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
    return list(grouper.values())


def diff_titles(pt_dup):
    #Generate the comparisons for the titles.
    #Currently compares the first two titles in a given set of pt_dup's
    title_diff=[]
    for occ in pt_dup:
        if occ[0].fields['title'] and occ[1].fields['title']:
            title1, title2 = (occ[i].fields['title'].replace(' ','\n')
                              .splitlines(keepends=True)+['\n'] for i in (0, 1))
            title_diff.append(''.join(difflib.ndiff(title1, title2)))
        else:
            title_diff.append('')
    return title_diff


def title_dump(entry):
    for inst in entry:
        print(inst.fields['title']+'\n')


def write_summary(pt_dup, title_diff, uniques, fname):
    s=''
    lines = '====================================\n\n'
    for i in range(len(pt_dup)):
        s+= lines
        s+= btx_io.write_bib_entries(pt_dup[i])+'\n\n'
        s+= title_diff[i]+'\n\n'

    s+=lines+'\n\n\n\Entries not matched to anything else by fuzzy comparison of titles'+lines
    for unq in uniques:
        s+= btx_io.write_bib_entries(unq)+'\n'

    if fname is not None:
        with open(fname, 'w', encoding='latin1') as f:
            f.write(s)
    return s

#Takes a list of fileneames and the out fname
def second_pass(filenames, fname=None, silent=False):
    in_ = list(btx_io.read_bib_entries(*filenames))
    if fname is None:
        fname = 'CITeX_annotated_' + os.path.basename(
            filenames[0]).replace('.txt', '.bib')
    group_year = group_entries(in_)
    pt_dup = []
    uniques = []
    for g in group_year:
        dups, unique_inst = compare.compare(g)
        for occ in dups: pt_dup.append(occ)
        for unq in unique_inst: uniques.append(unq)
    title_diff = diff_titles(pt_dup)
    write_summary(pt_dup, title_diff, uniques, fname)

    if not silent:
        print('There are {} references in the input {}'.format(
              len(in_), 'files' if len(filenames) > 1 else 'file'))
        print('{} references were found with no heuristic match of title'.format(len(uniques)))
        print('{} sets of references have been highlighted for your attention in '.format(len(pt_dup))+str(fname))
    return pt_dup, title_diff


def get_args():
    parser = argparse.ArgumentParser(description=__doc__.strip())
    parser.add_argument('-V', '--version', action='version',
                        version=dedupe.__version__)
    parser.add_argument('files', type=str, nargs='+',
                        help='the filenames to process')
    parser.add_argument('-o', '--out_file', help='output filename (or auto)')
    return parser.parse_args()


def console():
    args = get_args()
    second_pass(args.files, args.out_file)

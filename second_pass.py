import collections
import unidecode
import string
import difflib
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
    return list(grouper.values())


def diff_titles(pt_dup):
    #Generate the comparisons for the titles.
    #Currently compares the first two titles in a given set of pt_dup's
    title_diff=[]
    for occ in pt_dup:
        if occ[0].fields['title'] and occ[1].fields['title']:
            title1, title2 = occ[0].fields['title'].replace(' ','\n'),occ[1].fields['title'].replace(' ','\n')
            diff = difflib.ndiff(title1.splitlines(keepends=True),title2.splitlines(keepends=True))       
            title_diff.append(''.join(diff))
        
        else:
            title_diff.append('')
            print(c)
            print(''.join(diff), end="")
        
    return title_diff
  
def title_dump(entry):
    for inst in entry:
        print(inst.fields['title']+'\n')

        
        
def write_summary(pt_dup, title_diff,fname):
    s=''
    lines = '=============================\n'
    for i in range(len(pt_dup)):
        s+= lines
        s+= btx_io.write_bib_entries(pt_dup[i])+'\n\n'
        s+= title_diff[i]+'\n\n'
        
    if fname is not None:
        with open(fname, 'w', encoding='latin1') as f:
            f.write(s)
    return s
    
    
def second_pass(*filenames,fname=None):
    in_ = list(btx_io.read_bib_entries(*filenames))
    
    group_year = group_entries(in_)

    pt_dup = []
    for g in group_year:
        for occ in compare.compare(g): pt_dup.append(occ)

    title_diff = diff_titles(pt_dup)
        
    write_summary(pt_dup, title_diff,fname)
    
    return pt_dup, title_diff
    
    


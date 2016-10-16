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

    
def second_pass(*filenames):
    in_ = list(btx_io.read_bib_entries(*filenames))
    
    group_year = group_entries(in_)

    pt_dup = []
    for g in group_year:
        for occ in compare.compare(g): pt_dup.append(occ)
    
    #Generate the comparisons for the titles.
    #Currently compares the first two titles in a given set of pt_dup's
    
    #for occ in pt_dup:
        
        
        
    '''
    btx_io.write_bib_entries(out, fname='dedup_' + os.path.basename(
        filenames[0]).replace('.txt', '.bib'))    
    '''
    
    
    
    return pt_dup


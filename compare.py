import unidecode
import string
import difflib


def compress_str(string_in,dump_thes=1):
    #convert to unicode
    cmp = unidecode.unidecode(string_in)
    #dump puncuation and white spaces
    cmp = "".join(s for s in cmp if s not in string.punctuation+' ').lower()
    if dump_thes:
        cmp = cmp.replace('the', '')
    return cmp
    

def compare(input_list):
    #Compressing {title} into an un-puncuated, un-spaced, un-cased string
    for entry in input_list:
        entry.cmp_title = compress_str(entry.fields.get('title', ''))

    div = [[input_list[0]]]
    for inp in input_list[1:]:
        for divj in div:
            divj_title = divj[0].cmp_title
            cmp_score = len(difflib.get_close_matches(divj_title, [inp.cmp_title], cutoff=0.9))
            if cmp_score:  #add duplicate
                divj.append(inp)
                break
        else:
            div.append([inp])

    dups=[]
    unique=[]
    for d in div:
        if len(d) > 1: dups.append(d)
        else: unique.append(d)                
    return dups, unique

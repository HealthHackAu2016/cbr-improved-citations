
import unidecode
import string
import distance


def compress_str(string_in,dump_thes=1):
    #convert to unicode
    cmp = unidecode.unidecode(string_in)
    #dump puncuation and white spaces
    cmp = "".join(s for s in cmp if s not in string.punctuation+' ')
    if dump_thes:
        cmp = cmp.replace('the', '')
    return cmp


def compare(input_list):
    #Compressing {title} into an un-puncuated, un-spaced, un-cased string
    for entry in input_list:
        entry.cmp_title = compress_str(entry.fields.get('title', ''))
        entry.cmp_journal = compress_str(entry.fields.get('journal', ''))

    div = [[input_list[0]]]
    for inp in input_list[1:]:
        for divj in div:
            cmp_score = distance.sorensen(inp.cmp_title, divj[0].cmp_title)
            if cmp_score < 0.2:  #add duplicate
                divj.append(inp)
                break
            div.append([inp])
    return div

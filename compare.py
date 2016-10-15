# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 15:41:43 2016

@author: Sam
"""
import re
import pybtex
from pybtex import database
import unidecode
import string
import distance

"""
s = open('./raw/MDR 2 before final.txt','r',encoding='latin1').read()
s = re.sub('}.','},',s)
db = database.parse_string(s, 'bibtex')

#test set 1
input_list = []
for entry in db.entries.keys[90:190]:
    input_list.append(db.entries[entry])
"""
       
     
def compress_str(string_in,dump_thes=1):    
    #convert to unicode
    cmp = unidecode.unidecode(string_in)
    #dump puncuation and white spaces
    cmp = "".join(s for s in cmp if s not in string.punctuation+' ')
    #dump the's
    if dump_thes: cmp = "".join(cmp.split('the'))
    return(cmp)
        

def compare(input_list):
    #Compressing {title} into an un-puncuated, un-spaced, un-cased string
    for entry in input_list:      
        if 'title' in entry.fileds:
            entry.cmp_title = compress_str(entry.fields['title'])
        else: entry.cmp_title = ''
        if 'journal' in entry.fileds:
            entry.cmp_journal = compress_str(entry.fields['journal'])
        else: entry.cmp_journal = ''
           
    div = [[input_list[0]]]
    for i in range(1,len(input_list)):
        for j in range(len(div)):
            cmp_score = distance.sorensen(input_list[i].cmp_title,div[j].cmp_title)
            if cmp_score < 0.2:  #add duplicate
                div[j].append(input_list[i])    
                break
            div.append([input_list[i]])
    return(div)
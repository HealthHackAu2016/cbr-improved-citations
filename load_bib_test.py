import re
import pybtex
from pybtex import database

s = open('./raw/MDR 2 before final.txt','r',encoding='latin1').read()
s = re.sub('}.','},',s)
db = database.parse_string(s, 'bibtex')
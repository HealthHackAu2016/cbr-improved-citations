""" USAGE: best_entry(duplicates)
RETURNS: Best of duplicates
"""

def score_citation_entry(entry):
    score = 0
    
    # each author listed is worth 2 other fields
    score += 2*len(entry.persons)
    score += len(entry.fields)
    
    # helllll no
    if 'title' not in entry.fields or entry.fields['title'] == '':
        score -= 10000
    if len(entry.persons) == 0:
        score -= 10000
    if 'year' not in entry.fields or entry.fields['year'] == '':
        score -= 10000
    
    # some are better than others
    if 'ISSN' in entry.fields:
        if len(entry.fields['ISSN'].split('ISSN')) > 1:
            score -= 1
        if len(entry.fields['ISSN'].split('(')) > 1:
            score -= 1
        if len(entry.fields['ISSN'].split(')')) > 1:
            score -= 1
            
    return score

def best_entry(entries):
    scores = list(map(score_citation_entry, duplicates))
    filt = list(map(lambda x: x == max(scores), scores))
   
    for i,good in enumerate(filt):
        print(good)
        if good:
            return entries[i]

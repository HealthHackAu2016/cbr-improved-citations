""" USAGE: best_entry(duplicates)
RETURNS: Best of duplicates
"""

def score_citation_entry(entry):
    score = 0

    # each author listed is worth 2 other fields
    score += 2*len(entry.persons)
    score += len(entry.fields)

    # helllll no
    if not entry.fields.get('title'):
        score -= 10000
    if len(entry.persons) == 0:
        score -= 10000
    if not entry.fields.get('year'):
        score -= 10000
    if not entry.fields.get('journal'):
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
    return sorted([(score_citation_entry(e), e) for e in entries],
                  key=lambda t: t[0])[-1][1]

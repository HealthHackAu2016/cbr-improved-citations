#! python3

import collections


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


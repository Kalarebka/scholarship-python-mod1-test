"""Using built-in function filter create function filter_with(), which filters out given data 
   to objects (list and/or dicts) that contains keyword. Function must filter nested containers.
   Usage of recursion is required"""

from data import data

# I'm making an assumption that if a parent structure contains the keyword, the child structures also have to stay
# Also assuming top structure in data is a list

def filter_with(data, keyword: str):
    for child_item in item:
        if isinstance(child_item, list):
            child_item = list(filter_with(contains_keyword, child_item))
        if isinstance(child_item, dict):
            child_item = dict(filter_with, child_item)
    return list(filter(lambda x: contains_keyword(x, keyword), data))


def contains_keyword(item, keyword: str):
    has_nested = any(isinstance(item, list) or isinstance(item, dict) for item in data)
    if has_nested:
        return filter_with(item, keyword)
    if not has_nested:
        if isinstance(item, list) and keyword in item:
            return True
        if isinstance(item, dict) and (keyword in item.keys() or keyword in item.values()):
            return True


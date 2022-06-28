"""Using built-in function filter create function filter_with(), which filters out given data 
   to objects (list and/or dicts) that contains keyword. Function must filter nested containers.
   Usage of recursion is required"""

"""It's ugly but it works"""

import json
import pprint

from data import data

pp = pprint.PrettyPrinter()

def is_list_or_dict(item):
    return isinstance(item, list) or isinstance(item, dict)

def contains_keyword(item, keyword):
    if is_list_or_dict(item):
        return keyword in json.dumps(item)
    return True

def has_nested_list_or_dict(data):
    if any(is_list_or_dict(item) for item in data):
        return True
    elif isinstance(data, dict):
        return any(is_list_or_dict(value) for value in data.values())

def filter_with(data, keyword):
    # Base case
    if not has_nested_list_or_dict(data):
        if isinstance(data, list):
            return list(filter(lambda item: contains_keyword(item, keyword), data))
        elif isinstance(data, dict):
            return dict(filter(lambda item: contains_keyword(item[1], keyword), data.items()))
    # Have to go deeper & data is a list?
    if isinstance(data, list):
        new_data = [filter_with(item, keyword) if is_list_or_dict(item) else item for item in data]
        return list(filter(lambda item: contains_keyword(item, keyword), new_data))
    # Have to go deeper & data is a dict?
    elif isinstance(data, dict):
        new_data = {key: filter_with(value, keyword) if is_list_or_dict(value) else value for key, value in data.items()}
        return dict(filter(lambda item: contains_keyword(item[1], keyword), new_data.items()))

for item in filter_with(data, "Gloria"):
    pp.pprint(item)
            
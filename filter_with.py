"""Using built-in function filter create function filter_with(), which filters out given data 
   to objects (list and/or dicts) that contains keyword. Function must filter nested containers.
   Usage of recursion is required"""

"""It's ugly but it works and does not use filter"""

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
            return [item for item in data if contains_keyword(item, keyword)]
        elif isinstance(data, dict):
            return {k: v for k, v in data.items() if contains_keyword(v, keyword)}
    # Have to go deeper & data is a list?
    if isinstance(data, list):
        new_data = [filter_with(item, keyword) if is_list_or_dict(item) else item for item in data]
        return [item for item in new_data if contains_keyword(item, keyword)]
    # Have to go deeper & data is a dict?
    elif isinstance(data, dict):
        new_data = {key: filter_with(value, keyword) if is_list_or_dict(value) else value for key, value in data.items()}
        return {k: v for k, v in new_data.items() if contains_keyword(v, keyword)}

        # list(filter(lambda item: contains_keyword(item, keyword), new_data))
        # dict(filter(lambda item: contains_keyword(item[1]), new_data.items()))

for item in filter_with(data, "Gloria"):
    pp.pprint(item)
            
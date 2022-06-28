"""Using built-in function filter create function filter_with(), which filters out given data 
   to objects (list and/or dicts) that contains keyword. Function must filter nested containers.
   Usage of recursion is required"""

"""DOES NOT WORK - I'm just leaving it here in case I think of some way to do it"""
import json
import pprint

from data import data

pp = pprint.PrettyPrinter()


# for item in filter_with(data, "Bruce Barton"):
#     pp.pprint(item)

def is_list_or_dict(item):
    return isinstance(item, list) or isinstance(item, dict)

def contains_keyword(item, keyword):
    return keyword in json.dumps(item)

def has_nested_list_or_dict(data):
    if any(is_list_or_dict(item) for item in data):
        return True
    elif isinstance(data, dict):
        return any(is_list_or_dict(value) for value in data.values())

def filterfilter(data, keyword):
    # Check if it's base case - data contains no objects that have nested lists or dicts
    base_case = True
    for item in data:
        if (is_list_or_dict(item)) and has_nested_list_or_dict(item):
            base_case = False
    if base_case:
        return data
    # Have to go deeper & data is a list?
    if isinstance(data, list):
        new_data = [filterfilter(item) if is_list_or_dict(item) else item for item in data]
        return 
    


            




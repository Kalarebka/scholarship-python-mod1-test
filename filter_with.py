"""Using built-in function filter create function filter_with(), which filters out given data 
   to objects (list and/or dicts) that contains keyword. Function must filter nested containers.
   Usage of recursion is required"""

"""DOES NOT WORK - I'm just leaving it here in case I think of some way to do it"""
import json
import pprint

from data import data

pp = pprint.PrettyPrinter()


def filter_with(data, keyword: str):
    return filter(lambda x: contains_keyword(x, keyword), data)

def contains_keyword(item, keyword):
    if has_nested_list_or_dict(data):
        return filter_with(item, keyword)
    return keyword in json.dumps(item)

def has_nested_list_or_dict(data):
    if any(isinstance(item, list) or isinstance(item, dict) for item in data):
        return True
    elif isinstance(data, dict):
        return any(isinstance(value, list) or isinstance(value, dict) for value in data.values())



for item in filter_with(data, "Bruce Barton"):
    pp.pprint(item)





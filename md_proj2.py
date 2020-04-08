from ast import literal_eval
import re
import numpy as np

def parse_date(x):
    if re.search(r'[\d]{1,2} [A-Za-z]{3}, [\d]{4}', x):
        return x.replace(',', '')
    elif re.search(r'[A-Za-z]{3} [\d]{4}', x):
        return '1 ' + x
    elif x == '':
        return np.nan
    else:
        print(x)

def eval_date(x):
    x = literal_eval(x)
    if x['coming_soon']:
        return '' # return blank string so can drop missing at end
    else:
        return x['date']

def combine_and_binary(column1, column2):
    """This function will compare the columns of developer and publisher,
    and return a Series of 1 (True) and 0 (False)"""

    series_results = column1 == column2
    series_results = series_results.apply(lambda x: 1 if x == True else 0)
    return series_results.to_frame()

def remove_item(list_of_items):
    if 'Indie' in list_of_items:
        list_of_items.remove('Indie')
    return list_of_items

def assign_genre(list_of_items):
    genre_list = ['Action', 'Adventure', 'Strategy', 'Racing', 'RPG', 'Casual']
    for item in list_of_items:
        if item in genre_list:
            return item
    return 'None'

def convert_platforms(platform):
    result = 0
    if "'windows': True" in platform:
        result += 1
    if "'mac': True" in platform:
        result += 1
    if "'linux': True" in platform:
        result += 1
    return result
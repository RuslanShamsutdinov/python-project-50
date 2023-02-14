from gendiff.utilities import load_file
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain


def generate_diff(filename1, filename2, format_result='stylish'):
    file1 = load_file('gendiff', 'tests', 'fixtures', filename1)
    file2 = load_file('gendiff', 'tests', 'fixtures', filename2)
    result = diff_dict(file1, file2)
    if format_result == 'stylish':
        return stylish(result)
    if format_result == 'plain':
        return plain(result)[:-1]


# flake8: noqa: C901
def diff_dict(old_dict, new_dict):
    result = {}
    for key, value in old_dict.items():
        if key in new_dict:
            if isinstance(value, dict) and isinstance(new_dict[key], dict):
                value = diff_dict(old_dict[key], new_dict[key])
                result[key] = {
                    'TYPE': 'NESTED',
                    'KEY': key,
                    'VALUE': value,
                }
            elif value == new_dict[key]:
                result[key] = {
                    'TYPE': 'UNCHANGED',
                    'KEY': key,
                    'VALUE': value,
                }
            else:
                result[key] = {
                    'TYPE': 'CHANGED',
                    'KEY': key,
                    'VALUE': {
                        'OLD': value,
                        'NEW': new_dict[key]
                    }}
        else:
            result[key] = {
                'TYPE': 'DELETED',
                'KEY': key,
                'VALUE': value
            }
    for key, value in new_dict.items():
        if key not in old_dict:
            result[key] = {
                'TYPE': 'ADDED',
                'KEY': key,
                'VALUE': value,
            }
    return result

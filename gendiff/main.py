from .utilities import load_file
from .formatters.stylish import stylish
from .formatters.plain import plain
from .formatters.json import json_format
from .diff_dict import diff_dict


def generate_diff(filename1, filename2, format_result='stylish'):
    file1 = load_file('gendiff', 'tests', 'fixtures', filename1)
    file2 = load_file('gendiff', 'tests', 'fixtures', filename2)
    result = diff_dict(file1, file2)
    if format_result == 'stylish':
        return stylish(result)
    if format_result == 'plain':
        return plain(result)[:-1]
    if format_result == 'json':
        return json_format(result)

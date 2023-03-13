from pathlib import Path
from .parser import parse
from .formatters.stylish import stylish
from .formatters.plain import plain
from .formatters.json import json_format
from .diff_dict import diff_dict


def generate_diff(filename1, filename2, format_result="stylish"):
    file1 = load_file("tests", "fixtures", filename1,
                      filetype=filename1.split('.')[1])
    file2 = load_file("tests", "fixtures", filename2,
                      filetype=filename1.split('.')[1])
    result = diff_dict(file1, file2)
    if format_result == "stylish":
        return stylish(result)
    if format_result == "plain":
        return plain(result)[:-1]
    if format_result == "json":
        return json_format(result)


def load_file(*args, filetype):
    path = Path(*args)
    with open(path) as file:
        return parse(file, filetype)

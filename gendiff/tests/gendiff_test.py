from gendiff import generate_diff
from gendiff.cli import parser_args
from gendiff.utilities import load_file
import pytest
import sys


@pytest.mark.parametrize('file1, file2, format_result, expected', [
    ('file1.json', 'file2.json', 'stylish',
     load_file('gendiff', 'tests', 'fixtures', 'result1')),
    ('file1.yml', 'file2.yml', 'stylish',
     load_file('gendiff', 'tests', 'fixtures', 'result1')),
    ('file3.json', 'file4.json', 'stylish',
     load_file('gendiff', 'tests', 'fixtures', 'result_stylish')),
    ('file3.json', 'file4.json', 'plain',
     load_file('gendiff', 'tests', 'fixtures', 'result_plain')),
    ('file3.json', 'file4.json', 'json',
     load_file('gendiff', 'tests', 'fixtures', 'result_json')),
])
def test_generate_diff(file1, file2, format_result, expected):
    diff = generate_diff(file1, file2, format_result)
    assert diff == expected


def test_parser_args():
    sys.argv = ['gendiff', '--format', 'plain', 'file1.json', 'file2.json']
    args = parser_args()
    assert args.first_file == 'file1.json'
    assert args.second_file == 'file2.json'
    assert args.format == 'plain'

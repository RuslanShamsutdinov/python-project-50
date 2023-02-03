from gendiff.gen_diff import generate_diff
from gendiff.cli import parser_args
from gendiff.utilities import load_file
import pytest
import sys


@pytest.mark.parametrize('file1, file2, expected', [
    ('file1.json', 'file2.json',
     load_file('gendiff', 'tests', 'fixtures', 'result1.txt')),
    ('file1.yml', 'file2.yml',
     load_file('gendiff', 'tests', 'fixtures', 'result1.txt')),
    ('file3.json', 'file4.json',
     load_file('gendiff', 'tests', 'fixtures', 'result2.txt')),
])
def test_generate_diff(file1, file2, expected):
    diff = generate_diff(file1, file2)
    assert diff == expected


def test_parser_args():
    sys.argv = ['gendiff', '--format', 'plain', 'file1.json', 'file2.json']
    args = parser_args()
    assert args.first_file == 'file1.json'
    assert args.second_file == 'file2.json'
    assert args.format == 'plain'

from gendiff import gen_diff
from gendiff.tools import load_file
import pytest


@pytest.mark.parametrize('file1, file2, expected', [
    ('file1.json', 'file2.json',
     load_file('gendiff', 'tests', 'fixtures', 'result.txt')),
    ('file1.yml', 'file2.yml',
     load_file('gendiff', 'tests', 'fixtures', 'result.txt'))])
def test_generate_diff(file1, file2, expected):
    diff = gen_diff(file1, file2)
    assert diff == expected

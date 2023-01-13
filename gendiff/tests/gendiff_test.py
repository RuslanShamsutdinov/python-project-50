from gendiff.generate_diff import gen_diff
from gendiff.open_file import load_file
import pytest


@pytest.mark.parametrize('file1, file2, expected', [('file1.json', 'file2.json', load_file('result.txt'))])
def test_generate_diff(file1, file2, expected):
    diff = gen_diff(file1, file2)
    assert diff == expected

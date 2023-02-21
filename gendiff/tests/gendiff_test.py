from gendiff import generate_diff
from gendiff.cli import parser_args
from gendiff.utilities import load_file
import pytest
import sys


@pytest.mark.parametrize(
    "file1, file2, format_result, expected",
    [
        (
            "file1.json",
            "file2.json",
            "stylish",
            load_file("gendiff", "tests", "fixtures", "result1_stylish.txt"),
        ),
        (
            "file1.yml",
            "file2.yml",
            "stylish",
            load_file("gendiff", "tests", "fixtures", "result1_stylish.txt"),
        ),
        (
            "file3.json",
            "file4.json",
            "stylish",
            load_file("gendiff", "tests", "fixtures", "result2_stylish.txt"),
        ),
        (
            "file3.json",
            "file4.json",
            "plain",
            load_file("gendiff", "tests", "fixtures", "result2_plain.txt"),
        ),
        (
            "file3.json",
            "file4.json",
            "json",
            load_file("gendiff", "tests", "fixtures", "result2_json.txt"),
        ),
    ],
)
def test_generate_diff(file1, file2, format_result, expected):
    diff = generate_diff(file1, file2, format_result)
    assert diff == expected


def test_parser_args():
    sys.argv = ["gendiff", "--format", "plain", "file1.json", "file2.json"]
    args = parser_args()
    assert args.first_file == "file1.json"
    assert args.second_file == "file2.json"
    assert args.format == "plain"

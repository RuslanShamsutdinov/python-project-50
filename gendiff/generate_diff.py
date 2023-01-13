import json
from pathlib import Path


def gen_diff(filename1, filename2):
    path1 = Path('gendiff', 'tests', 'fixtures', filename1)
    path2 = Path('gendiff', 'tests', 'fixtures', filename2)
    with open(path1) as f1:
        file1 = json.load(f1)
    with open(path2) as f2:
        file2 = json.load(f2)
    result = {}
    for i in sorted(list(set(file1) - set(file2))):
        result[('- ' + i)] = file1[i]
    for i in sorted(list(set(file2) & set(file1))):
        if file1[i] == file2[i]:
            result['  ' + i] = file1[i]
        else:
            result[('- ' + i)] = file1[i]
            result[('+ ' + i)] = file2[i]
    for i in sorted(list(set(file2) - set(file1))):
        result[('+ ' + i)] = file2[i]
    return ((str(result)).replace("'", "")).replace(",", "\n")

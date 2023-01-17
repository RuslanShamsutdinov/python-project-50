from gendiff.tools import load_file


def gen_diff(filename1, filename2):
    file1 = load_file('gendiff', 'tests', 'fixtures', filename1)
    file2 = load_file('gendiff', 'tests', 'fixtures', filename2)
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

from pathlib import Path


def load_file(filename1):
    path1 = Path('gendiff', 'tests', 'fixtures', filename1)
    with open(path1) as file:
        return file.read()




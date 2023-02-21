from pathlib import Path
import json
import yaml


def load_file(*args):
    path = Path(*args)
    with open(path) as file:
        if Path(*args).suffix == ".json":
            return json.load(file)
        elif Path(*args).suffix == ".yml":
            return yaml.safe_load(file)
        else:
            return file.read()


def multiple_replace(target_str, replace_words):
    for i, j in replace_words.items():
        target_str = target_str.replace(i, j)
    return target_str

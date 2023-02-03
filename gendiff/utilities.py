from pathlib import Path
import json
import yaml


def load_file(*args):
    path = Path(*args)
    with open(path) as file:
        if Path(*args).suffix == '.json':
            return json.load(file)
        elif Path(*args).suffix == '.yml':
            return yaml.safe_load(file)
        else:
            return file.read()

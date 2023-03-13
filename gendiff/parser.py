import json
import yaml


def parse(file, filetype):
    if filetype == "json":
        return json.load(file)
    elif filetype in {"yml", "yaml"}:
        return yaml.safe_load(file)
    else:
        raise ValueError('Unknown file extension')

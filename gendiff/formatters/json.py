from gendiff.formatters.stylish import diff_to_concatenated_dict
import json


def json_format(diff):
    json_line = json.dumps(diff_to_concatenated_dict(diff), indent=4)
    return json_line

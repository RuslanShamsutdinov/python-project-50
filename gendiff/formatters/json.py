from gendiff.formatters.stylish import diff_to_concatenated_dict
from gendiff.utilities import multiple_replace
import json


def json_format(diff):
    json_line = json.dumps(diff_to_concatenated_dict(diff), indent=4)
    # replace_values = {',': '', '"': '', ': \n': ':\n'}
    # result = multiple_replace(json_line, replace_values)
    return json_line

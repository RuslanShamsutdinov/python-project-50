from gendiff.utilities import multiple_replace
from gendiff.diff_dict import diff_to_concatenated_dict


def stylish(result_dict):
    def dict_to_string(Dict, lvl=0):
        tab = '  '
        result_string = ''
        for key in Dict:
            if isinstance(Dict[key], dict):
                result_string += f'{tab * (lvl + 1)}{key}: ' \
                                 f'{{\n{dict_to_string(Dict[key], lvl + 2)}  ' \
                                 f'{tab * (lvl + 1)}}}\n'
            else:
                result_string += f'{tab * (lvl + 1)}{key}: {Dict[key]}\n'
        return result_string

    replace_values = {"False": "false", "True": "true",
                      "None": "null"}
    string = f'{{\n{dict_to_string(diff_to_concatenated_dict(result_dict))}}}'
    result = multiple_replace(string, replace_values)
    return result

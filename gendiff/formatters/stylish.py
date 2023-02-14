# flake8: noqa: C901
def diff_to_dict(diff):
    result = {}
    print(diff)
    def add_space(value):
        result = {}
        if isinstance(value, dict):
            for nested_key, nested_value in value.items():
                result[f'  {nested_key}'] = add_space(nested_value)
        else:
            return value
        return result

    for key, value in sorted(diff.items()):
        if value['TYPE'] == 'NESTED':
            result[f'  {key}'] = diff_to_dict(value['VALUE'])
        if value['TYPE'] == 'UNCHANGED':
            result[f'  {key}'] = add_space(value['VALUE'])
        if value['TYPE'] == 'CHANGED':
            result[f'- {key}'] = add_space(value['VALUE']['OLD'])
            result[f'+ {key}'] = add_space(value['VALUE']['NEW'])
        if value['TYPE'] == 'ADDED':
            result[f'+ {key}'] = add_space(value['VALUE'])
        if value['TYPE'] == 'DELETED':
            result[f'- {key}'] = add_space(value['VALUE'])
    return result


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

    def multiple_replace(target_str, replace_words):
        for i, j in replace_words.items():
            target_str = target_str.replace(i, j)
        return target_str

    replace_values = {"False": "false", "True": "true",
                      "None": "null", ": \n": ":\n"}
    string = f'{{\n{dict_to_string(diff_to_dict(result_dict))}}}'
    result = multiple_replace(string, replace_values)
    return result

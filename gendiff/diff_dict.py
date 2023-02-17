# flake8: noqa: C901
def diff_dict(old_dict, new_dict):
    result = {}
    for key, value in old_dict.items():
        if key in new_dict:
            if isinstance(value, dict) and isinstance(new_dict[key], dict):
                value = diff_dict(old_dict[key], new_dict[key])
                result[key] = {
                    'TYPE': 'NESTED',
                    'KEY': key,
                    'VALUE': value,
                }
            elif value == new_dict[key]:
                result[key] = {
                    'TYPE': 'UNCHANGED',
                    'KEY': key,
                    'VALUE': value,
                }
            else:
                result[key] = {
                    'TYPE': 'CHANGED',
                    'KEY': key,
                    'VALUE': {
                        'OLD': value,
                        'NEW': new_dict[key]
                    }}
        else:
            result[key] = {
                'TYPE': 'DELETED',
                'KEY': key,
                'VALUE': value
            }
    for key, value in new_dict.items():
        if key not in old_dict:
            result[key] = {
                'TYPE': 'ADDED',
                'KEY': key,
                'VALUE': value,
            }
    return result


def diff_to_concatenated_dict(diff):
    result = {}

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
            result[f'  {key}'] = diff_to_concatenated_dict(value['VALUE'])
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

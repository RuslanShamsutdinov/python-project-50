# flake8: noqa: C901
NESTED = "NESTED"
UNCHANGED = "UNCHANGED"
CHANGED = "CHANGED"
DELETED = "DELETED"
ADDED = "ADDED"


def diff_dict(old_dict, new_dict):
    result = {}
    for key, value in old_dict.items():
        if key in new_dict:
            if isinstance(value, dict) and isinstance(new_dict[key], dict):
                value = diff_dict(old_dict[key], new_dict[key])
                result[key] = {
                    "TYPE": NESTED,
                    "KEY": key,
                    "VALUE": value,
                }
            elif value == new_dict[key]:
                result[key] = {
                    "TYPE": UNCHANGED,
                    "KEY": key,
                    "VALUE": value,
                }
            else:
                result[key] = {
                    "TYPE": CHANGED,
                    "KEY": key,
                    "VALUE": {"OLD": value, "NEW": new_dict[key]},
                }
        else:
            result[key] = {"TYPE": DELETED, "KEY": key, "VALUE": value}
    for key, value in new_dict.items():
        if key not in old_dict:
            result[key] = {
                "TYPE": ADDED,
                "KEY": key,
                "VALUE": value,
            }
    return result




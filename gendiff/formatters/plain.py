# flake8: noqa: C901
import gendiff.diff_dict as dd


def plain(diff, path=""):
    def output_matching(input_value):
        match_dict = {True: "true", 0: "0", False: "false", None: "null"}
        if isinstance(input_value, dict):
            return "[complex value]"
        elif input_value in match_dict:
            if type(input_value) == int:
                return 0
            else:
                return match_dict[input_value]
        else:
            return f"'{input_value}'"

    result = ""
    for key, value in sorted(diff.items()):
        key = f"{path}.{key}" if path else key
        if value["TYPE"] == dd.NESTED:
            result += plain(value["VALUE"], f"{key}")
        elif value["TYPE"] == dd.CHANGED:
            result += (
                f"Property '{key}' was updated. From "
                f"{output_matching(value['VALUE']['OLD'])} "
                f"to {output_matching(value['VALUE']['NEW'])}\n"
            )
        elif value["TYPE"] == dd.UNCHANGED:
            result += ""
        elif value["TYPE"] == dd.ADDED:
            result += (
                f"Property '{key}' was added with value: "
                f"{output_matching(value['VALUE'])}\n"
            )
        elif value["TYPE"] == dd.DELETED:
            result += f"Property '{key}' was removed\n"
    return result

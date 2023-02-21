import argparse


def parser_args():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument(
        "-f", "--format", help='output format (default: "stylish")',
        default="stylish"
    )
    return parser.parse_args()

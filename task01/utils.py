import argparse
from typing import Any


def argparse_positive_int_checker(value: Any) -> int:
    try:
        int_value = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f'{value} is not int value')

    if int_value <= 0:
        raise argparse.ArgumentTypeError(f'{value} is not positive int')

    return int_value


def add_parser_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-f',
        type=str,
        required=True,
        dest='filepath',
        help='filepath to parse',
    )
    parser.add_argument(
        '-n',
        type=argparse_positive_int_checker,
        required=False,
        default=200,
        dest='max_substr_len',
        help='maximum number of characters in substring',
    )
    parser.add_argument(
        '-l',
        action='store_true',
        required=False,
        default=False,
        dest='split_score',
        help='keep lines with "score" solid',
    )
    parser.add_argument(
        '-d',
        type=str,
        required=False,
        default=None,
        dest='dirpath',
        help='dirpath to write substring files',
    )
    parser.add_argument(
        '-r',
        type=str,
        required=False,
        default=None,
        dest='eval_code',
        help='dirpath to write substring files',
    )


def get_parsed_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    add_parser_args(parser)
    return parser.parse_args()

# Файл обеспечивает взаимодействие программы с пользователем
# Модуль выполняте Артём Рожков git: Art-me-plz


import argparse


def add_parser_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-f',
        type=str,
        required=True,
        dest='filepath',
        help='filepath to parse',
    )
    parser.add_argument(
        '-of',
        action='store_true',
        required=False,
        default=False,
        dest='__take_func',
        help='--output-functions',
    )
    parser.add_argument(
        '-od',
        action='store_true',
        required=False,
        default=False,
        dest='directives',
        help='directives to parse',
    )
    parser.add_argument(
        '-ot',
        action='store_true',
        required=False,
        default=False,
        dest='__take_typedef',
        help='typedefs to parse',
    )
    parser.add_argument(
        '-j',
        type=str,
        required=False,
        default=False,
        dest='savespace',
        help='file to save',
    )



def get_parsed_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    add_parser_args(parser)
    return parser.parse_args()

def main(argc: list[str]) -> int:
    pass

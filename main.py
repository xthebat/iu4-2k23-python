import argparse
import os


def add_parser_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-f',
        type=str,
        help='Путь к файлу',
        dest='filepath',
        required=True,
    )
    parser.add_argument(
        '-n',
        type=int,
        help='Максимальная длина строки',
        dest='max_num',
        default=200,
    )
    parser.add_argument(
        '-d',
        type=str,
        help='Директория для записи',
        dest='dirpath',
        default='',
    )


def process_file(input: str, max_num: int) -> list[str]:
    result = []

    i = 0
    while i < len(input):
        if i + max_num >= len(input):
            result.append(input[i:])
            break
        
        i_space = input.rfind(' ', i + 1, i + max_num)
        if i_space == -1:
            print('Не удалось разбить входную строку')
            return []

        result.append(input[i:i_space])
        i = i_space

    return result


def print_substrings(substrings: list[str]) -> None:
    for index, substr in enumerate(substrings):
        print(f'Substring #{index}:')
        print(substr)


def write_substrings(substrings: list[str], dirpath: str) -> None:
    for index, substr in enumerate(substrings):
        filepath = os.path.join(dirpath, f'substring_{index}.txt')
        with open(filepath, 'wt') as fout:
            fout.write(substr)


def main():
    parser = argparse.ArgumentParser()
    add_parser_args(parser)
    args = parser.parse_args()

    if args.max_num <= 0:
        print('Длина строки должна быть больше 0')
        return -1

    if not os.path.exists(args.filepath):
        print('Путь к файлу указан не правильно или файл не существует')
        return -1

    if args.dirpath and not os.path.exists(args.dirpath):
        print('Директория указана не правильно')
        return -1

    with open(args.filepath, 'rt') as fin:
        input = fin.read()

    substrings = process_file(input, args.max_num)
    if args.dirpath:
        write_substrings(substrings, args.dirpath)
    else:
        print_substrings(substrings)


if __name__ == '__main__':
    main()

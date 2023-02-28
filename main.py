import argparse
import os


def add_parser_args(parser):
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


def process_file(input, max_num):
    result = []

    i = 0
    while i < len(input):
        if i + max_num >= len(input):
            result.append(input[i:])
            break

        if input[i + max_num] == ' ':
            result.append(input[i : i + max_num])
            i = i + max_num
            continue

        i_space = input.rfind(' ', i, i + max_num)
        if i_space == -1:
            print('Не удалось разбить входную строку')
            return []

        result.append(input[i:i_space])
        i = i_space

    return result


def print_s(substrings):
    i = 1
    for s in substrings:
        print(f'Substring #{i}:')
        print(s)
        i += 1


def write_s(substrings, dirpath):
    i = 1
    for s in substrings:
        with open(os.path.join(dirpath, f'substring_{i}.txt'), 'wt') as fout:
            fout.write(s)
        i += 1


def main():
    parser = argparse.ArgumentParser()
    add_parser_args(parser)
    args = parser.parse_args()

    if args.max_num <= 0:
        print('Длина строки должна быть больше 0')
        return

    if not os.path.exists(args.filepath):
        print('Путь к файлу указан не правильно или файл не существует')
        return

    if args.dirpath and not os.path.exists(args.dirpath):
        print('Директория указана не правильно')
        return

    with open(args.filepath, 'rt') as fin:
        input = fin.read()

    substrings = process_file(input, args.max_num)
    if args.dirpath:
        write_s(substrings, args.dirpath)
    else:
        print_s(substrings)


if __name__ == '__main__':
    main()

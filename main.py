from argparse import *
from argparse import Namespace
from sys import stderr

DEFAULT_CHAR_LIMIT = 200


def load_file(filename_: str) -> str:
    try:
        with open(file=filename_, mode='r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        log(text_=f'[ERROR] Can\'t open file with name <{filename_}>!', is_terminate_=True)


def log(text_: str, is_terminate_: bool = False) -> None:
    print(text_, file=stderr)
    if is_terminate_:
        exit(1)


def split_str(string_: str, char_limit_: int, is_full_score_: bool = False) -> list[str]:
    raw_stringlist = string_.strip().split('\n')
    stringlist = []

    for line in raw_stringlist:
        if is_full_score_ and 'score' in line:
            stringlist.append(line + '\n')
            if len(line) > char_limit_:
                log(text_=f'[ERROR] Can\'t parse word with chosen maximum number of chars!', is_terminate_=True)
            continue
        words = line.split(' ')
        for word in words:
            if len(word) > char_limit_:
                log(text_=f'[ERROR] Can\'t parse word with chosen maximum number of chars!', is_terminate_=True)
            stringlist.append(word)
        stringlist.append('\n')

    return stringlist


def merge_tags(words_: list[str]) -> list[str]:
    tag_start = None
    for index, word in enumerate(words_):
        if word.startswith('@') and word.endswith(':'):
            continue
        if word.startswith('@'):
            tag_start = index
            continue
        if tag_start is not None:
            words_[tag_start] += ' ' + word
            words_[index] = ''
        if word.endswith(':') and tag_start is not None:
            tag_start = None
            continue

    while '' in words_:
        words_.remove('')

    return words_


def group_words(words_: list[str], char_limit_: int) -> list[str]:
    data = []
    substring = ''

    for word in words_:
        if word == '\n':
            substring += word
            continue
        if word.endswith('\n'):
            if len(word) + len(substring) <= char_limit_:
                substring += word
                continue
            data.append(substring)
            substring = word
            continue
        if len(word) + len(substring) <= char_limit_:
            substring += word + ' '
            continue

        data.append(substring)
        substring = word

    if substring != '':
        data.append(substring)

    return data


def handle_data(string_, char_limit_, is_full_score_) -> list[str]:
    words = split_str(string_=string_, char_limit_=char_limit_, is_full_score_=is_full_score_)
    words = merge_tags(words_=words)
    data = group_words(words_=words, char_limit_=char_limit_)

    return data


def filter_data(data_: list[str], requirement_: str) -> tuple[str]:
    return tuple(filter(eval(requirement_), data_))


def print_data(data_: list[str] or tuple[str]) -> None:
    for i, substr in enumerate(data_):
        print(f'Substring #{i}')
        print(f'{substr}')


def dump_data(data_: list[str] or tuple[str], outdir_: str = None) -> None:
    for i, substr in enumerate(data_):
        try:
            with open(file=f'{outdir_}/substring_{i}', mode='w', encoding='utf-8') as file:
                file.write(f'Substring #{i}\n')
                file.write(f'{substr}')
        except FileNotFoundError:
            log(text_=f'[ERROR] Can\'t open directory <{outdir_}>!\n', is_terminate_=True)


def parse_args() -> Namespace:
    parser = ArgumentParser(description="Best py prog ever!")
    parser.add_argument('-f', '--filename',
                        dest='filename',
                        required=True,
                        nargs=1,
                        metavar='<filename>',
                        help='input File name'
                        )
    parser.add_argument('-n', '--number',
                        dest='char_limit',
                        required=False,
                        nargs=1,
                        default=DEFAULT_CHAR_LIMIT,
                        metavar='<chars number>',
                        help='maximum Number of chars in the string'
                        )

    parser.add_argument('-l', '--line',
                        dest='is_whole_line',
                        required=False,
                        default=None,
                        action='store_true',
                        help='key with no args, indicates, '
                             'that you can\'t separate `score` Line')
    parser.add_argument('-d', '--dir',
                        dest='dir',
                        required=False,
                        nargs=1,
                        metavar='<directory>',
                        help='output Directory'
                        )
    parser.add_argument('-r', '--requirement',
                        dest='req',
                        required=False,
                        nargs=1,
                        metavar='<lambda-func>',
                        help='bonus Requirement for parser')

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    try:
        limit = int(args.char_limit[0])
    except ValueError:
        limit = DEFAULT_CHAR_LIMIT
    if limit < 0:
        log(f'[ERROR] Maximum number of characters in line is negative', is_terminate_=True)

    filestring = load_file(filename_=args.filename[0])
    parsed_data: list = handle_data(string_=filestring, char_limit_=limit, is_full_score_=args.is_whole_line)

    if args.req:
        parsed_data: tuple = filter_data(data_=parsed_data, requirement_=args.req[0])

    if args.dir:
        dump_data(data_=parsed_data, outdir_=args.dir[0])
        exit(0)
    print_data(data_=parsed_data)


if __name__ == '__main__':
    main()

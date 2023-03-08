import os
from typing import List
from typing import Optional

import utils


class BaseError(Exception):
    pass


class ParseError(BaseError):
    pass


_TAG_OPENING_CHAR = '@'
_TAG_CLOSING_CHAR = ':'
_SUBSTR_TITLE = 'Substring #{index}:'
_SUBSTR_FILE_TITLE = 'substring_{index}.txt'
_SCORE_KEY = 'score'


def tag_is_not_closed(word: str) -> bool:
    return word[0] == _TAG_OPENING_CHAR and word[-1] != _TAG_CLOSING_CHAR


def merge_by_rules(
        row_words: List[str], split_score: bool, eval_code: Optional[str],
) -> List[str]:
    if split_score and _SCORE_KEY in row_words:
        return [' '.join(row_words)]

    if eval_code:
        try:
            row_checker = eval(eval_code, {'__builtins__': None})
        except:
            raise ParseError('failed to eval custom rule')
        if not row_checker(row_words):
            return [' '.join(row_words)]

    return row_words


def merge_tags(row_words: List[str]) -> List[str]:
    result_words: List[str] = []

    for word in row_words:
        if not result_words:
            result_words.append(word)
            continue

        if tag_is_not_closed(result_words[-1]):
            result_words[-1] += ' ' + word
            continue

        result_words.append(word)

    if result_words and tag_is_not_closed(result_words[-1]):
        raise ParseError(f'failed to find end of tag: {result_words[-1]}')

    return result_words


def add_substr_to_arr(
        substr: str, substr_arr: List[str], max_substr_len: int,
) -> None:
    substr = substr.strip()
    if len(substr) > max_substr_len:
        raise ParseError(f'substr len={len(substr)} more then max: {substr}')

    substr_arr.append(substr)


def parse_file(
        filepath: str,
        max_substr_len: int,
        split_score: bool,
        eval_code: Optional[str],
) -> List[str]:
    row_words_arr: List[List[str]] = []
    with open(filepath, 'rt') as f_in:
        for row in f_in:
            words = merge_by_rules(row.split(), split_score, eval_code)
            words = merge_tags(words)
            row_words_arr.append(words)

    substr_arr: List[str] = []
    current_substr = ''
    for row_words in row_words_arr:
        is_first = True
        for word in row_words:
            if not is_first:
                current_substr += ' '
            is_first = False

            if len(current_substr) + len(word) <= max_substr_len:
                current_substr += word
                continue

            add_substr_to_arr(current_substr, substr_arr, max_substr_len)
            current_substr = word + ' '
            is_first = True

        current_substr += '\n'

    add_substr_to_arr(current_substr, substr_arr, max_substr_len)

    return substr_arr


def print_substr_arr(substr_arr: List[str], dirpath: Optional[str]):
    index = 0
    for substr in substr_arr:
        index += 1

        if not dirpath:
            print(_SUBSTR_TITLE.format(index=index), substr, sep='\n')
            continue

        with open(
                os.path.join(dirpath, _SUBSTR_FILE_TITLE.format(index=index)),
                'wt',
        ) as f_out:
            f_out.write(substr)


def main():
    args = utils.get_parsed_args()

    try:
        substr_arr = parse_file(
            args.filepath,
            args.max_substr_len,
            args.split_score,
            args.eval_code,
        )
        print_substr_arr(substr_arr, args.dirpath)
    except (FileExistsError, FileNotFoundError) as exc:
        print(exc)
    except ParseError as exc:
        print('failed to parse file:', exc)


if __name__ == '__main__':
    main()

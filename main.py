import sys
import os.path


def get_param(argv: list[str], key: str, param: str) -> str or None:
    pos_key = argv.index(key)

    if pos_key + 1 >= len(argv):
        print(f"After {key} require {param}. Read documentation!")
        exit(-1)
    else:
        return argv[pos_key + 1]


def check_key(argv: list[str], key: str) -> None:
    if key not in argv:
        print(f"Key {key} not found")
        exit(-1)


def check_file(argv: list[str]) -> None:
    file_name = get_param(argv, "-f", "file name")

    if not os.path.exists(file_name):
        print(f"File {file_name} not found")
        exit(-1)


def check_necessary_params(argv: list[str]) -> None:
    if len(argv) == 1:
        print("List args is empty")
        exit(-1)
    elif len(argv) > 7:
        print("List args is very big")
        exit(-1)

    check_key(argv, "-f")
    check_file(argv)


def parse_params(argv: list[str]) -> dict:
    params = {
        "file": "",
        "num": 200,
        "-l": False,
        "-d": False,
    }

    file = argv[argv.index("-f") + 1]

    params["file"] = file

    if "-n" in argv:
        num = argv[argv.index("-n") + 1]
        if num.isdigit():
            params["num"] = int(num)

    if "-l" in argv:
        params["-l"] = True

    if "-d" in argv:
        params["-d"] = True

    return params


def issplit(row: str, pos: int, cur_len: int, num: int) -> bool:
    if pos == len(row):
        return True

    if "@" in row[pos]:
        return len(row[pos]) + len(row[pos + 1]) + cur_len <= num
    else:
        return True


def join_word(params: dict, word_list: list[str]) -> list[str]:
    string_list = []
    num = params["num"]

    cur_len = 0
    s = ""
    first = True
    for row in word_list:
        for (pos, word) in enumerate(row):
            if len(word) > num:
                print("This file cannot be divided into substrings")
                exit(-1)

            if not first:
                s += " "
                cur_len = len(s)

            if len(word) + cur_len <= num and issplit(row, pos, cur_len, num):
                s += word
                cur_len = len(s)
                first = False
            else:
                string_list.append(s)
                s = word
                cur_len = len(s)

        s += '\n'
        cur_len = len(s)
        first = True

    string_list.append(s)
    return string_list


def parse_file(params: dict) -> list[str]:
    word_list = []
    with open(params["file"], 'rt') as file:
        for row in file:
            row_split = row.split()
            while "" in row_split:
                row_split.remove("")

            word_list.append(row_split)

    return join_word(params, word_list)


def print_substrings(substrings: list[str]) -> None:
    for (i, row) in enumerate(substrings):
        print(f"Substring #{i + 1}:")
        print(row)


def write_file_substrings(substrings: list[str]) -> None:
    for (i, row) in enumerate(substrings):
        with open(f'substring_{i + 1}.txt', 'wt') as file:
            file.write(row)


def main() -> int:
    check_necessary_params(sys.argv)
    params = parse_params(sys.argv)
    substrings = parse_file(params)
    if "-d" in sys.argv:
        write_file_substrings(substrings)
    else:
        print_substrings(substrings)

    return 0


if __name__ == '__main__':
    main()

# -f task1.txt -n 200

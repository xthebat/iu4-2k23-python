import os.path
import sys


# Func handles args
def args_handler(argv: list[str]) -> dict or int:
    args_dict = {"-f": "",
                 "-n": 200,
                 "-l": False,
                 "-d": False}

    args_set = {"-f", "-n", "-l", "-d"}

    if len(argv) < 2:
        print("Not enough arguments")
        return -1

    if '-f' in argv:
        f_index = argv.index('-f')
    else:
        print("No '-f' argument")
        return -1

    if (f_index + 1) < len(argv):
        if argv[f_index + 1] not in args_set:
            file_name = argv[f_index + 1]
            args_dict["-f"] = f"{file_name}"
        else:
            print("-f argument should have file name after it")
            return -1

    if not os.path.exists(file_name):
        print("No such file")
        return -1

    if '-n' in argv:
        n_index = argv.index('-n')
        substr_len_index = n_index + 1
        if substr_len_index < len(argv):
            if argv[substr_len_index] not in args_set and argv[substr_len_index].isdigit():
                args_dict["-n"] = int(argv[substr_len_index])

    if '-l' in argv:
        args_dict["-l"] = True

    if '-d' in argv:
        d_index = argv.index('-d')
        args_dict["-d"] = ".\\"
        if (d_index + 1) < len(argv) - 1:
            if argv[d_index + 1] not in args_set:
                args_dict["-d"] = argv[d_index + 1]

    return args_dict


# Func creates list of username-tag indexes
# These indexes are skipped while separating file strings
def find_tag_exceptions(file_str: str) -> list[int]:
    at_ptr = 0
    tag_exception_indexes = []
    for i in range(file_str.count('@')):
        at_ptr = file_str[at_ptr:].find('@') + 1
        if len(tag_exception_indexes) < 1:
            tag_exception_indexes.append(at_ptr)
        else:
            tag_exception_indexes.append(at_ptr + tag_exception_indexes[-1])
        for j in range(file_str[tag_exception_indexes[-1]:].find(':')):
            tag_exception_indexes.append(tag_exception_indexes[-1] + 1)
        at_ptr += 1
    return tag_exception_indexes


# Func finds spaces or \n as separate indexes
def find_sep_indexes(file_str: str, tag_exception_indexes: list[int], max_substring_len: int, line_sep_flag: bool, ) -> \
        list[int] or int:
    high_sep_index = 0
    sep_indexes: list[int] = [0]

    while high_sep_index < len(file_str):
        low_sep_index = high_sep_index
        high_sep_index = low_sep_index + max_substring_len + 1

        sep_space = ' ' if not line_sep_flag else ''

        if high_sep_index >= len(file_str):
            high_sep_index = len(file_str)
        else:
            if (sep_space or '\n') not in file_str[low_sep_index:high_sep_index]:
                print('String cannot be split up with respect to the given constraints')
                return -1
            elif high_sep_index in tag_exception_indexes and not line_sep_flag:
                high_sep_index = file_str[:high_sep_index].rfind('@')
            else:
                high_sep_index = file_str[:high_sep_index].rfind(sep_space or '\n') + 1

        sep_indexes.append(high_sep_index)

    return sep_indexes


# Func prints out substrings to files or I/O
def print_substrings(file_str: str, sep_indexes: list[int], output_file_path: str or bool):
    number_of_substrings = len(sep_indexes) - 1
    if not output_file_path:
        for it in range(number_of_substrings):
            print(f'Substring #{it + 1}')
            print(f'Substring length: {sep_indexes[it + 1] - sep_indexes[it]}')
            substring_list = file_str[sep_indexes[it]:sep_indexes[it + 1]].split("\n")
            for substring_line in substring_list:
                print(f'\t{substring_line}')
            print()
    else:
        for it in range(number_of_substrings):
            file_name = f'{output_file_path}substring_{it + 1}.txt'
            with open(file_name, 'w', encoding="UTF-8") as f:
                f.write(f'Substring #{it + 1}; \n')
                f.write(f'Substring length: {sep_indexes[it + 1] - sep_indexes[it]}\n')
                substring_list = file_str[sep_indexes[it]:sep_indexes[it + 1]].split("\n")
                for substring_line in substring_list:
                    f.write(f'\t{substring_line}\n')
        print("Output files generated successfully")


def main(argv: list[str]) -> int:
    if (args_dict := args_handler(argv)) == -1:
        return -1
    else:
        file_name = args_dict["-f"]
        max_substring_len = args_dict["-n"]
        line_sep_flag = True if args_dict["-l"] else False
        output_file_path = False if not args_dict["-d"] else args_dict["-d"]

    with open(f'{file_name}', 'rt', encoding="utf-8") as f:
        file_str = f.read()

    tag_exception_indexes = find_tag_exceptions(file_str)

    if (sep_indexes := find_sep_indexes(file_str, tag_exception_indexes, max_substring_len, line_sep_flag)) == -1:
        return -1

    print_substrings(file_str, sep_indexes, output_file_path)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))

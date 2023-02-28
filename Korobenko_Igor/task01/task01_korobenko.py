import sys


def main(args: list[str]):
    read_args = check_param(args)
    split_arr = string_division(read_args)
    sym_limit = int(read_args[1])
    result_arr = substring_create(split_arr, sym_limit)
    string_print(result_arr)

    return 0

    # АРГУМЕНТЫ ПРОВЕРИТЬ ПО-ДРУГОМУ


def check_param(args: list[str]):  # проверить
    if len(args) < 2:
        sys.exit('ERROR 100: not enough parameters')

    read_args = []

    # Проверка f параметра
    if '-f' in args:
        f_param = args.index('-f')
    else:
        sys.exit('ERROR 101: no "-f" parameter')

    try:
        f_path_param = args[f_param + 1]
        read_args.append(f_path_param)
    except:
        sys.exit('ERROR 1010: no file path')

    if f_path_param.find('.txt', 0, len(f_path_param)) == -1:
        sys.exit('ERROR 102: file has no .txt extension')

    # Проверка -n параметра

    if '-n' in args:
        n_param = args.index('-n')
    else:
        sys.exit('ERROR 103: no "-n" parameter')

    try:
        n_num = args[n_param + 1]
        read_args.append(n_num)
    except:
        sys.exit('ERROR 1030: no value of -n param')

    return read_args


def string_division(args: list[str]):
    file_name = args[0]
    try:
        file = open(f"{file_name}")
        text = file.read()
    except FileNotFoundError:
        sys.exit('ERROR 200: file not found')

    # запись строк в массив строк
    split_arr = []
    for line in text.splitlines():
        split_arr.append(line)
    file.close()

    if split_arr[len(split_arr) - 1] == '\n':
        del split_arr[len(split_arr)]

    return split_arr


def substring_create(split_arr: list[str], sym_limit: int):
    # образование подстрок
    result_arr = ['']
    substring_num = 0
    temp_substring_sym = 0
    # for i in range(0, len(split_arr)):
    #     if len(split_arr[i]) > sym_limit:
    #         sys.exit(f"ERROR 300: string #{i + 1} is too long for division\nYou can change -n parameter")
    #     if (len(result_arr[substring_num]) + len(split_arr[i])) < sym_limit:
    #         result_arr[substring_num] += split_arr[i] + '\n'
    #     else:
    #         substring_num += 1
    #         result_arr.append(split_arr[i] + '\n')

    for i in range(0, len(split_arr)):
        # Если невозможно прибавить всю строку в подстроку, то нужно делить
        if len(split_arr[i]) + temp_substring_sym > sym_limit:
            max_addition_len = sym_limit - len(split_arr[i])
            temp_str = split_arr[i]
            index = find_separation_sym(split_arr[i], max_addition_len)
            result_arr[substring_num] += temp_str[0:index] + '\n'
            result_arr.append('')
        # Если можно добавить всю строку, то сразу добавляем в подстроку
        else:
            result_arr[substring_num] += split_arr[i] + '\n'
            temp_substring_sym += len(result_arr[substring_num])

    result_arr[substring_num] = result_arr[substring_num].removesuffix('\n')

    return result_arr


def find_separation_sym(string: str, max_addition_len: int) -> int:
    index = 0
    if string.find('@', index, max_addition_len) != -1:
        index = string.find('@', index, max_addition_len)
        if string.find(':', index, max_addition_len) != -1:
            index = string.find(':', index, max_addition_len)

    while index < max_addition_len:
        index = string.find(' ', index, max_addition_len)

    return index


def string_print(result_arr: list[str]):
    for i in (range(0, len(result_arr))):
        print(f'Substring #{i + 1}\n{result_arr[i]}')


if __name__ == '__main__':
    sys.exit(main(sys.argv))

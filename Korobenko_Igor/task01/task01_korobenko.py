import sys


def main(args: list[str]) -> int:
    read_args = check_param(args)
    error_print(read_args)
    split_arr = string_division(read_args)
    if split_arr == -1:
        sys.exit('ERROR: file is not found')
    result_arr = substring_create(split_arr, int(read_args[1]), read_args[2])
    string_print(result_arr)

    return 0


def check_param(args: list[str]) -> list[str | bool | int]:
    min_len = 2
    max_len = 5
    if len(args) < min_len:
        sys.exit('ERROR: not enough parameters')
    if len(args) > max_len:
        sys.exit('ERROR: too many parameters')

    read_args = []

    if '-f' in args:
        f_param = args.index('-f')
        try:
            f_path_param = args[f_param + 1]
            read_args.append(f_path_param)
        except:
            read_args.append(False)
    else:
        read_args.append(False)

    if '-n' in args:
        n_param = args.index('-n')

        try:
            n_num = args[n_param + 1]
            read_args.append(n_num)
        except:
            read_args.append(False)
    else:
        n_num = -1
        read_args.append(n_num)
        print('There will be no strict symbol number substrings')

    is_l_argument_appeared = True if '-l' in args else False
    read_args.append(is_l_argument_appeared)

    return read_args

    # read_args: [-f val] [-n_val] [-l_val]


def error_print(args: list[str | bool]) -> None:
    if not args[0]:
        sys.exit('ERROR: no "-f" parameter')
    if not args[0].endswith('.txt'):
        sys.exit('ERROR: file has no .txt extension')
    if not args[1]:
        return None
    else:
        if int(args[1]) < -1:
            sys.exit('ERROR: invalid -n parameter value')
    return None


def string_division(args: list[str]) -> int | list[str]:
    file_name = args[0]
    try:
        file = open(file_name, encoding='utf-8')
        text = file.read()
    except:
        return -1
    file.close()

    # запись строк в массив строк
    split_arr = text.splitlines()

    return split_arr


def substring_create(split_arr: list[str], sym_limit: int, flag_l: bool) -> list[str]:
    # образование подстрок
    result_arr = ['']
    if sym_limit == -1:
        for string in split_arr:
            result_arr[0] += string + '\n'
        result_arr[0].removesuffix('\n')
        return result_arr
    # инициализация переменных индекса, номера подстроки и числа символов в рассматриваемой подстроке
    substring_num = 0
    temp_substring_sym = 0
    index = 0

    # Если выставлен флаг -l, то просто делим строки на подстроки с учетом ограничения
    if flag_l:
        for i in range(0, len(split_arr)):
            if len(split_arr[i]) > sym_limit:
                sys.exit(f"ERROR: string #{i + 1} is too long for division\nYou can change -n parameter")
            if (len(result_arr[substring_num]) + len(split_arr[i])) < sym_limit:
                result_arr[substring_num] += split_arr[i] + '\n'
            else:
                substring_num += 1
                result_arr.append(split_arr[i] + '\n')
    else:
        # иначе проходимся по списку разделенных строк и делим на подстроки по словам
        for i in range(0, len(split_arr)):
            # Если невозможно прибавить всю строку в подстроку, то нужно делить строку
            if len(split_arr[i]) + temp_substring_sym > sym_limit:
                # определяем максимальное число символов, которое мы можем добавить в подстроку
                max_addition_len = sym_limit - temp_substring_sym
                temp_str = split_arr[i]

                # определяем индекс, до которого мы можем скопировать строку в подстроку
                index = find_separation_symbol(split_arr[i], max_addition_len, index)
                result_arr[substring_num] += temp_str[0:index]
                result_arr.append('')
                substring_num += 1
                temp_substring_sym = 0

                if len(temp_str[index:len(temp_str)]) > temp_substring_sym:
                    result_arr[substring_num] += temp_str[index:len(temp_str)] + '\n'
                    index = 0
                else:
                    # если строка длинная, то нужно провести вышеописанные операции в цикле несколько раз
                    i -= 1

            # Если можно добавить всю строку, то сразу добавляем в подстроку
            else:
                result_arr[substring_num] += split_arr[i] + '\n'

            # Записываем результирующее значение
            temp_substring_sym = len(result_arr[substring_num])

        result_arr[substring_num] = result_arr[substring_num].removesuffix('\n')

    return result_arr


def find_separation_symbol(string: str, max_addition_len: int, index: int) -> int:
    if string.find('@', index, max_addition_len) != -1:
        if string.find(':', index, max_addition_len) != -1:
            index = string.find(':', index, max_addition_len)
    else:
        words = string.split()
        for word in words:
            if len(word) + index > max_addition_len:
                return index
            else:
                index += len(word) + 1
    return index + 1


def string_print(result_arr: list[str]):
    for i, substr in enumerate(result_arr):
        print(f'Substring #{i + 1}\n{substr}')


if __name__ == '__main__':
    sys.exit(main(sys.argv))

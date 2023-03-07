import sys


def main(args: list[str]):
    read_args = check_param(args)
    split_arr = string_division(read_args)
    result_arr = substring_create(split_arr, int(read_args[1]), read_args[2])
    string_print(result_arr)

    return 0


def check_param(args: list[str]):  # проверить
    global d_param
    if len(args) < 2:
        sys.exit('ERROR 100: not enough parameters')
    if len(args) > 5:
        sys.exit('ERROR 1000: too many parameters')

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

    read_args.append(False)
    if '-l' in args:
        read_args[2] = True

    return read_args


def string_division(args: list[str]):
    file_name = args[0]
    try:
        file = open(f"{file_name}", encoding='utf-8')
        text = file.read()
    except FileNotFoundError:
        sys.exit('ERROR 200: file is not found')

    # запись строк в массив строк
    split_arr = []
    for line in text.splitlines():
        split_arr.append(line)
    file.close()

    if split_arr[len(split_arr) - 1] == '\n':
        del split_arr[len(split_arr)]

    return split_arr


def substring_create(split_arr: list[str], sym_limit: int, flag_l: bool):
    # образование подстрок
    result_arr = ['']
    # инициализация переменных индекса, номера подстроки и числа символов в рассматриваемой подстроке
    substring_num = 0
    temp_substring_sym = 0
    index = 0

    # Если выставлен флаг -l, то просто делим строки на подстроки с учетом ограничения
    if flag_l:
        for i in range(0, len(split_arr)):
            if len(split_arr[i]) > sym_limit:
                sys.exit(f"ERROR 300: string #{i + 1} is too long for division\nYou can change -n parameter")
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
                index = find_separation_sym(split_arr[i], max_addition_len, index)
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


def find_separation_sym(string: str, max_addition_len: int, index: int) -> int:
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
    for i in (range(0, len(result_arr))):
        print(f'Substring #{i + 1}\n{result_arr[i]}')


if __name__ == '__main__':
    sys.exit(main(sys.argv))

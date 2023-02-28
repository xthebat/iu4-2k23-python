import sys


def print_data(data_splitter, count_substr):
    print("Substring #", count_substr, ":")
    print(f"{data_splitter}")


def main() -> int:  # объявление функции
    error_code = check_input_data()
    if error_code != 0:
        return error_code

    key_index = sys.argv.index('-f')
    file_name = sys.argv[key_index + 1]
    print(file_name)
    input_file = open(file_name, mode='r', encoding='utf-8')

    max_length_str = 200
    for it in sys.argv:
        if it == '-n':
            try:
                max_length_str = sys.argv[sys.argv.index('-n') + 1]
            except IndexError:
                print("нет числа после -n")
                return -4
            break

    data = input_file.read()
    input_file.close()

    length_str = len(data)
    i = 0
    count_substr = 1
    while i <= length_str - 1:
        if i + max_length_str - 1 <= length_str - 1:
            last = i + max_length_str - 1
        else:
            last = length_str - 1

        if last != length_str - 1:
            while data[last] != ' ' and data[last + 1] != ' ' and data[last] != '\n' and data[last + 1] != '\n':
                last = last - 1
                if last < i:
                    sys.exit("user-friendly")

        tag_start = -1
        for j in range(i, last + 1, 1):
            if (data[j] == '@'):
                tag_start = j
        point_access = -1
        if (tag_start != -1):
            for j in range(tag_start, last + 1, 1):
                if (data[j] == ':'):
                    point_access = 1
        if point_access == -1 and tag_start != -1:
            last = tag_start - 1
            if tag_start == i:
                sys.exit("user-friendly")

        data_splitter = data[i:last + 1]
        print_data(data_splitter, count_substr)
        count_substr = count_substr + 1
        i = last + 1

    return 0


def check_input_data() -> int:  # проверка на ошибку входных данных
    try:
        key_index = sys.argv.index('-f')
    except ValueError:
        print('Отсутствует ключ -f')
        return -1
    try:
        sys.argv[key_index + 1]
    except IndexError:
        print('Отсутствует строка названия входного файла')
        return -2
    try:
        input_file = open(sys.argv[key_index + 1], mode='r', encoding='utf-8')
        input_file.close()
    except FileNotFoundError:
        print('Файл не существует')
        return -3

    return 0


if __name__ == '__main__':  # начало кода
    main()

import sys


def print_data(char, count) -> None:
    print(f'Substring #{count}:\n')
    print(char)
    return


# проверка агрумента -n и длины строки
def check_input_parameter() -> int:
    try:
        sys.argv.index('-n')
        max_length_str = int(sys.argv[sys.argv.index('-n') + 1])
    except ValueError:
        if not sys.argv.index('-n'):
            sys.exit('Введены некорректные данные')
        if not max_length_str:
            max_length_str = 200

    return max_length_str


def splitter_file(file_name: str) -> list:
    max_length_str = check_input_parameter()
    line_data = []
    i = 0
    count = 1
    char = ''

    with open(file_name, mode='r', encoding='utf-8') as input_file:
        str_data = input_file.readlines()  # -> [str_1, str_2, str_3]
        for line in str_data:
            line_data.extend(line.split())
            line_data.append('\n')

    for index in range(len(line_data)):
        if not line_data[index]:
            continue
        if line_data[index][0] == '@':
            line_data[index] += ' ' + line_data[index + 1] + line_data[index + 2]
            line_data[index + 1] = ''
            line_data[index + 2] = ''

    print(line_data)

    for word in line_data:
        if len(char) + len(word) <= max_length_str:
            if not word:
                continue
            if word[0] == '-':
                char += '\t'
            char += word + ' '
            continue
        print_data(char, count)
        count += 1
        char = ''
        char += word + ' '
        print_data(char, count)
        char = ''
        count += 1


def main() -> int:  # объявление функции
    error_code = check_input_data()
    if error_code:
        return error_code

    key_index = sys.argv.index('-f')
    file_name = sys.argv[key_index + 1]
    splitter_file(file_name)

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

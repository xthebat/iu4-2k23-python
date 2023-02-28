import argparse

# функция, которая разделяет входные строки на подстроки
def split_string(input_string, max_length):
    # проверка на ограничение символов
    if len(input_string) <= max_length:
        return [input_string]

    # создаём пустой список куда загрузим результат
    substrings = []

    #  цикл по входной строке который разделяет на подстроки
    start_index = 0
    while start_index < len(input_string):
        end_index = start_index + max_length

        # мзбегаем разделение в середине слова
        if end_index < len(input_string) and not input_string[end_index].isspace() and not input_string[end_index-1].isspace():
            # нахождение ближайшего пробела справа
            near_space = input_string.find(" ", end_index)
            if near_space == -1:
                near_space = len(input_string)

            # нахождение ближайшего пробела слева
            last_space = input_string.rfind(" ", start_index, end_index)

            # изменяем индекс, чтобы корректно разделить строку
            if near_space - end_index <= end_index - last_space:
                end_index = near_space
            else:
                end_index = last_space

        # добавление подстроки в список
        substrings.append(input_string[start_index:end_index])#.strip())

        start_index = end_index

    return substrings

# функция вывода подстроки
def print_substrings(substrings):
    for i, substring in enumerate(substrings):
        print(f"Substring {i+1}: {substring}")

def main():
    # парсим аргументы
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Path to input file", required=True)
    parser.add_argument("-n", "--max-length", help="Maximum length of substring", type=int, default=200)
    args = parser.parse_args()

    # читаем файл
    with open(args.file, "r", encoding="utf-8") as f:
        input_string = f.read()

    # разбиваем строки на подстроки
    substrings = split_string(input_string, args.max_length)

    # выводим результат
    print_substrings(substrings)

if __name__ == "__main__":
    main()

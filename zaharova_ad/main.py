import sys


# --------------------Чтения файла--------------------------

def open_file(file_split_data):
    if '-f' not in sys.argv:
        print('Error parameter')
        sys.exit(0)

    filename = sys.argv[sys.argv.index('-f') + 1]

    with open(file=filename, mode='r', encoding='utf-8') as file:
        file_data = file.readlines()  # -> [str_1, str_2, str_3]
        if '-l' in sys.argv:
            file_split_data = bonus_param_l(file_data)
            return file_split_data
        for line in file_data:
            file_split_data.extend(line.split())  # str_1 -> [word_1, word_2, ...]
            file_split_data.append('\n')
        return file_split_data


# --------------------Bonus 1---------------------------
def bonus_param_l(file_data):
    file_split_data = []

    for line in file_data:
        if line[0] == '-':
            file_split_data.append(line)
            continue
        file_split_data.extend(line.split())
        file_split_data.append('\n')

    return file_split_data


# --------------------Объединение ников под одно слово---------------------------

def merge_words(file_split_data: list):
    nickname_index = None

    for i in range(len(file_split_data)):
        if not file_split_data[i]:
            continue
        if file_split_data[i][0] == '@' and file_split_data[i][-1] != ':':
            nickname_index = i
        if nickname_index is not None:
            file_split_data[nickname_index] += ' ' + file_split_data[i + 1]
            if file_split_data[i + 1][-1] == ':':
                nickname_index = None
            file_split_data[i + 1] = ''
    return file_split_data


# -----------------------Получить подстроки,ограниченные по длине-------------------------------

def split_line(file_split_data: list):
    if '-n' not in sys.argv:
        print('Error parameter')
        sys.exit(0)

    result = ''
    substring = ''
    i = 1
    char_number = int(sys.argv[sys.argv.index('-n') + 1])

    if not int(sys.argv[sys.argv.index('-n') + 1]):
        char_number = 200

    for index in range(len(file_split_data)):
        if len(substring) + len(file_split_data[index]) <= char_number:
            if not file_split_data[index]:
                continue
            if file_split_data[index][0] == '-':
                substring += '\t'
            substring += file_split_data[index]
            if file_split_data[index][-1] != '\n':
                substring += ' '
            continue
        result += f'Substring #{i}:\n' + substring + '\n'
        if '-d' in sys.argv:
            save_file(substring, i)
        substring = ''
        if file_split_data[index][0] == '-':
            substring += '\t'
        substring += file_split_data[index] + ' '
        i += 1

    result += f'Substring #{i}:\n' + substring + '\n'
    if '-d' in sys.argv:
        save_file(substring, i)
    print_line(result)


# -------------Bonus 2---------------------

def save_file(result, index_sub):
    sub_file = open(f'substring_{index_sub}.txt', 'w')
    sub_file.write(f'{result}\n')
    sub_file.close()
    return


# -----------------------------Вывод строки---------------------
def print_line(result):
    print(result)


def main():
    data = []
    data = open_file(data)
    if '-l' not in sys.argv:
        data = merge_words(data)
    split_line(data)


if __name__ == '__main__':
    main()

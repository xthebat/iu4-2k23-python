import sys


# Code 1 - incorrect parameter -f
# Code 2 - incorrect parameter -n


# --------------------Проверка аргументов командной строки--------------------------
def check_parameter():
    if '-f' not in sys.argv:
        sys.exit('Error parameter with code 1')
    if '-n' not in sys.argv:
        sys.exit('Error parameter with code 2')
    if '-d' in sys.argv:
        return 1
    if '-l' in sys.argv:
        return 2

    return 0


# --------------------Чтения файла и разделение на строки--------------------------

def read_split_file(file_split_data):
    filename = sys.argv[sys.argv.index('-f') + 1]

    with open(filename, 'r', encoding='utf-8') as file:
        file_data = file.readlines()  # -> [str_1, str_2, str_3]
        check_result = check_parameter()
        if check_result == 2:
            file_split_data = merge_line_tag(file_data)
            return file_split_data
        for line in file_data:
            file_split_data.extend(line.split())  # str_1 -> [word_1, word_2, ...]
            file_split_data.append('\n')

    return file_split_data


# --------------------Bonus 1---------------------------
def merge_line_tag(file_data):
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

    for index in range(len(file_split_data)):
        if not file_split_data[index]:
            continue
        if file_split_data[index][0] == '@' and file_split_data[index][-1] != ':':
            nickname_index = index
        if nickname_index is not None:
            file_split_data[nickname_index] += ' ' + file_split_data[index + 1]
            if file_split_data[index + 1][-1] == ':':
                nickname_index = None
            file_split_data[index + 1] = ''
    return file_split_data


# -----------------------Получить подстроки,ограниченные по длине-------------------------------

def split_line(file_split_data: list):
    check_parameter()
    result = ''
    substring = ''
    i = 1

    try:
        char_number = int(sys.argv[sys.argv.index('-n') + 1])
    except ValueError:
        char_number = 200

    for word in file_split_data:
        if len(word) > char_number:
            sys.exit('Cant split line,-n value is too small')
        if len(substring) + len(word) <= char_number:
            if not word:
                continue
            if word[0] == '-':
                substring += '\t'
            substring += word
            if word[-1] != '\n':
                substring += ' '
            continue
        result += f'Substring #{i}:\n' + substring + '\n'
        print(result)
        substring = ''
        if word[0] == '-':
            substring += '\t'
        substring += word + ' '
        check_result = check_parameter()
        if check_result == 1:
            save_file(result, i)
        result = ''
        i += 1

    result += f'Substring #{i}:\n' + substring + '\n'
    check_result = check_parameter()
    if check_result == 1:
        save_file(result, i)
    print(result)


# -------------Bonus 2---------------------

def save_file(result, index_sub):
    with open(f'substring_{index_sub}.txt', 'w') as file:
        file.write(f'{result}\n')
    return


# ------------------Вызов функций---------------------

def main():
    check_parameter()
    data = []
    data = read_split_file(data)
    merge_lines = merge_words(data)
    split_line(merge_lines)


if __name__ == '__main__':
    main()

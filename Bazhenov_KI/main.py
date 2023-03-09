import sys


def processing_and_cropping_str(text, max_cnt, index_inc, l_rule):
    start_index = 0
    cnt = start_index
    end_index = -1
    text_length = len(text)
    list_of_str = []
    while cnt != text_length + 1:
        if text_length - cnt < index_inc:
            one_of_lines = text[start_index:text_length]
            list_of_str.append(one_of_lines)
            break
        while (cnt <= max_cnt) and cnt != text_length:
            if text[cnt] == '@':
                cnt_save = cnt
                temp = text.find(':', cnt, text_length - 1)
                if temp < (max_cnt - 1) and temp != -1:
                    cnt = temp + 1
                    if l_rule == 1:
                        cnt += 1
                        while text[cnt].isnumeric() == 1:
                            cnt += 1
                            if text[cnt] == text[-1]:
                                break
                        if cnt >= max_cnt and end_index == -1:
                            return
                        if cnt >= max_cnt:
                            cnt = cnt_save + 1
                elif temp == -1:
                    cnt += 1
                elif end_index == -1:
                    return
                else:
                    one_of_lines = text[start_index:end_index]
                    list_of_str.append(one_of_lines)
                    start_index = end_index + 1
                    max_cnt = start_index + index_inc
            if text[cnt] == ' ' or text[cnt] == '\n':
                end_index = cnt
                if cnt - 1 < max_cnt:
                    cnt += 1
            else:
                cnt += 1
        if end_index == -1:
            return
        one_of_lines = text[start_index:end_index]
        list_of_str.append(one_of_lines)
        start_index = end_index + 1
        end_index = -1
        max_cnt = start_index + index_inc
        cnt = start_index
    return list_of_str


def print_string(list_of_str, d_rule, file_dir) -> int:
    cnt = 0
    file_cnt = cnt + 1
    while cnt != len(list_of_str):
        if d_rule == 1:
            with open(f"{file_dir}str{str(file_cnt)}.txt", "w") as new_file:
                new_file.write(list_of_str[cnt])
            file_cnt += 1
        print(list_of_str[cnt])
        cnt += 1
    return 0


def main() -> int:
    l_rule = 0
    d_rule = 0
    file_dir = []
    if len(sys.argv) == 1 or sys.argv.index('-f') == -1 or sys.argv.index('-n') == -1:
        print('Введены недопустимые параметры. Введите -f "путь к файлу" -n "Максимальное количество символов" -l -d')
        return 0
    file_path = sys.argv[sys.argv.index('-f') + 1]
    max_cnt = int(sys.argv[sys.argv.index('-n') + 1]) + 1
    if len(sys.argv) > 4:
        if sys.argv.index('-l') == -1 and sys.argv.index('-d') == -1:
            print('Введены недопустимые параметры.')
            return 0
        if sys.argv.index('-l') != -1:
            l_rule = 1
        if sys.argv.index('-d') != -1:
            d_rule = 1
            file_dir = sys.argv[sys.argv.index('-d') + 1]
    index_inc = max_cnt
    with open(file_path, "r") as file:
        text = file.read()
    list_of_str = processing_and_cropping_str(text, max_cnt, index_inc, l_rule)
    if list_of_str is None:
        print('Невозможно разделить следующую строку')
        exit(-1)
    print_string(list_of_str, d_rule, file_dir)
    print('Строки разделены')


if __name__ == '__main__':
    main()

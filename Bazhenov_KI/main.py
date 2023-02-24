import sys

def processing_and_cropping_str(text, max_index, start_index, INDEX_INC, l_rule, d_rule, file_cnt) -> int:
    cnt = start_index
    end_index = -1
    text_length = len(text)
    if cnt == text_length + 1:
        print('Строки разделены')
        return 0
    if text_length - cnt < INDEX_INC:
            if print_string(text_length, max_index, text, start_index, INDEX_INC, l_rule, d_rule, file_cnt) == 0:
                return 0
    while ((cnt <= max_index) and cnt != text_length):
        if text[cnt] == '@':
            cnt_save = cnt
            temp = text.find(':', cnt, text_length - 1)
            if temp < (max_index - 1) and temp != -1:
                cnt = temp + 1
                if (l_rule == 1):
                    cnt += 1
                    while text[cnt].isnumeric() == 1:
                        cnt += 1
                        if text[cnt] == text[-1]:
                            break
                    if cnt >= max_index and end_index == -1:
                        print('Невозможно разделить следующую строку ')
                        return 0
                    if cnt >= max_index:
                        cnt = cnt_save + 1
            elif temp == -1:
                cnt += 1
            elif end_index == -1:
                print('Невозможно разделить следующую строку ')
                return 0
            else:
                if print_string(end_index, max_index, text, start_index, INDEX_INC, l_rule, d_rule, file_cnt) == 0:
                    return 0
        if text[cnt] == ' ' or text[cnt] == '\n':
            end_index = cnt
            if cnt - 1 < max_index:
                cnt += 1
        else:
            cnt += 1
    if end_index == -1:
        print('Невозможно разделить строку')
        return 0
    if print_string(end_index, max_index, text, start_index, INDEX_INC, l_rule, d_rule, file_cnt) == 0:
        return 0

def print_string(end_index, max_index, text, start_index, INDEX_INC, l_rule, d_rule, file_cnt) -> int:
    final_str = text[start_index:end_index]
    if d_rule == 1:
        with open (sys.argv[7] + "str" + str(file_cnt) + ".txt", "w") as new_file:
            new_file.write("%s" % final_str)
        file_cnt += 1
    print(final_str)
    start_index = end_index + 1
    max_index = start_index + INDEX_INC
    if processing_and_cropping_str(text, max_index, start_index, INDEX_INC, l_rule, d_rule, file_cnt) == 0:
        return 0

def main(args: list[str]) -> int:
    l_rule = 0
    d_rule = 0
    print('Введите -f "путь к файлу" -n "Максимальное количество символов"')
    if len(sys.argv) == 1:
         print('Введены недопустимые параметры. Введите -f "путь к файлу" -n "Максимальное количество символов" -l -d')
         return 0
    else:
        param_name = sys.argv[1]
    if param_name == '-f':
        FILE_PATH = sys.argv[2]
    else:
        print(f'Неизвесный параметр {param_name}')
        return 0
    param_name = sys.argv[3]
    if param_name == '-n':
        max_index = int(sys.argv[4]) + 1
    else:
        print(f'Неизвесный параметр {param_name}')
        return 0
    if len(sys.argv) > 4:
        param_name = sys.argv[5]
        if param_name == '-l':
            l_rule = 1
        else:
            print(f'Неизвесный параметр {param_name}')
            return 0
    if len(sys.argv) > 5:
        param_name = sys.argv[6]
        if param_name == '-d':
            d_rule = 1
        else:
            print(f'Неизвесный параметр {param_name}')
            return 0

    INDEX_INC = max_index
    file_cnt = 1
    with open (sys.argv[2], "r") as file:
        text = file.read()
    start_index = 0
    if (processing_and_cropping_str(text, max_index, start_index, INDEX_INC, l_rule, d_rule, file_cnt) == 0):
        return 0

if __name__=='__main__':
    main(sys.argv)
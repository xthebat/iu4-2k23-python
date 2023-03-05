import sys
import re


def args_handler(args: list[str]) -> bool or dict:
    args_values = {}

    if '-f' in args:
        f_pos = args.index('-f')
        # Проверка, что после аргумента -f действительно записан путь к файлу или имя файла
        if re.match('(\w:.+)|(.+\.\w+)', args[f_pos + 1]):
            f_name = args[f_pos + 1]
            args_values["-f"] = f"{f_name}"
        else:
            print("Отсутствует, либо введены неверно     путь файла или его имя, если он расположен в корне")
            return False
    else:
        print("Отсутствует аргумент -f")
        return False

    if '-n' in args:
        n_pos = args.index('-n')
        # Проверка, что после -n действительно записано число
        if re.match('\d+', args[n_pos + 1]):
            n_value = args[n_pos + 1]
            args_values["-n"] = int(n_value)
        else:
            print("Отсутствует значение -n")
            return False
    else:
        print("Отсутствует аргумент -n")
        return False

    if '-d' in args:
        args_values["-d"] = True
    else:
        args_values["-d"] = False

    if '-l' in args:
        args_values["-l"] = True
    else:
        args_values["-l"] = False

    return args_values


def convert_text_to_tokens(words: list[str]) -> list[str]:
    tokens = []
    i = 0
    while i < len(words):
        word_i = words[i]
        if word_i.startswith('@'):
            if word_i.endswith(':') or word_i.endswith('/n'):
                tokens.append(word_i)
                i += 1
            else:
                tokens.append(word_i + ' ' + words[i + 1])
                i += 2
        else:
            tokens.append(word_i)
            i += 1
    return tokens


def convert_tokens_to_substrings(tokens: list[str], n: int) -> list[str] or bool:
    sub_strings = []
    buffer = []
    for token in tokens:
        if sum([len(x) for x in buffer]) + len(token) + len(buffer) - 1 <= n:
            buffer.append(token)
        elif len(token) > n:
            sub_strings.append(token)
            return False
        else:
            sub_strings.append(' '.join(buffer))
            buffer.clear()
            buffer.append(token)
    sub_strings.append(' '.join(buffer))
    return sub_strings


def search_newscore_strings_pos_len(words: list[str]) -> tuple:
    position = []
    length = []
    i = 0
    while i < len(words):
        if words[i] == ('-') and words[i + 1] == ('Новый'):
            position.append(i)
            k = i
            while k < len(words):
                if words[k].endswith('\n'):
                    length.append(k - i)
                    break
                k += 1
        i += 1
    return position, length


def convert_newscore_strings_to_connected_tokens(position: list[int], length: list[int], words: list[str]) -> list[str]:
    tokens = []
    buffer = []
    i = k = j = 0
    while i < len(words):
        if i == position[j]:
            while k <= length[j]:
                buffer.append(words[i])
                k += 1
                i += 1
            k = 0
            tokens.append(' '.join(buffer))
            buffer.clear()
            j += 1
            i -= 1
            if j == len(position):
                j = -1
        else:
            tokens.append(words[i])
        i += 1

    return tokens


def print_in_console_and_file(string: str, sub_strings: list[str], args_values: dict):
    # Убираем лишние пробелы
    formatted_string = re.sub(' \n ', '\n', string)
    if args_values["-d"]:
        with open('substring_{}.txt'.format(sub_strings.index(string) + 1), "w") as file:
            file.write(formatted_string)
    print('Substring #{}:'.format(sub_strings.index(string) + 1))
    if args_values["-l"]:
        print(f'{formatted_string}')
    else:
        print(f'{formatted_string}\n')


def main(args: list[str]) -> int:
    args_values = args_handler(args)

    if args_values:
        with open(args_values["-f"], 'rt', encoding="utf-8") as f:
            text = f.read()
            words = re.findall(r'[^ \n]+|\n', text)
    else:
        print("Что-то пошло не так, советую ознакомиться с документацией :)")
        return -1

    if args_values["-l"]:
        position, length = search_newscore_strings_pos_len(words)
        connected_tokens = convert_newscore_strings_to_connected_tokens(position, length, words)
        sub_strings = convert_tokens_to_substrings(connected_tokens, args_values["-n"])
    else:
        tokens = convert_text_to_tokens(words)
        sub_strings = convert_tokens_to_substrings(tokens, args_values["-n"])

    # Проверка что не вернулось значение False
    if sub_strings:
        for string in sub_strings:
            print_in_console_and_file(string, sub_strings, args_values)
    else:
        print("Некоторые слова или токены больше значения аргумента n и не могут быть разделены")
        return -1

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))

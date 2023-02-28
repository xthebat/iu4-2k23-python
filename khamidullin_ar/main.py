import sys
import re


def file_handler(args: list[str]) -> bool or dict:
    args_values = {}

    if '-f' in args:
        f_pos = args.index('-f')
        if re.match('(\w:.+)|(.+\.\w+)', args[f_pos + 1]):
            f_name = args[f_pos + 1]
            args_values["-f"] = f"{f_name}"
        else:
            print("Отсутствует путь файла или его имя, если он расположен в корне")
            return False
    else:
        print("Отсутствует аргумент -f")
        return False

    if '-n' in args:
        n_pos = args.index('-n')
        if re.match('\d+', args[n_pos + 1]):
            n_value = args[n_pos + 1]
            args_values["-n"] = int(n_value)
        else:
            print("Отсутствует значение -n")
            return False
    else:
        print("Отсутствует аргумент -n")
        return False
    return args_values


def text_to_tokens(words: str) -> list[str]:
    tokens = []
    i = 0
    while i < len(words):
        if words[i].startswith('@'):
            if words[i].endswith(':') or words[i].endswith(':/n'):
                tokens.append(words[i])
                i += 1
            else:
                tokens.append(words[i] + ' ' + words[i + 1])
                i += 2
        else:
            tokens.append(words[i])
            i += 1
    return tokens


def tokens_to_substrings(tokens: list[str], n: int) -> list[str] or bool:
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


def main(args: list[str]) -> int:
    args_values = file_handler(args)

    if args_values:
        with open(args_values["-f"], 'rt') as f:
            words = f.read().split(' ')
    else:
        print("Что-то пошло не так, советую ознакомиться с документацией :)")
        return -1

    tokens = text_to_tokens(words)
    sub_strings = tokens_to_substrings(tokens, args_values["-n"])

    if sub_strings:
        for string in sub_strings:
            print('Substring #{}:'.format(sub_strings.index(string) + 1))
            print(f'{string}\n')
    else:
        print("Некоторые слова или токены больше значения аргумента n и не могут быть разделены")
        return -1

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))

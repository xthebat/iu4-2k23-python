# Bondarenko UI4-82B
# With bonus 1

import sys
import re


def glue_nickname(words: list[str]):
    pop_numbers = []
    start_num = 0

    k = 1
    for j, word in enumerate(words):
        # print(word)
        if word.startswith('@'):
            start_num = j
        if word.endswith(':') and j > start_num:
            end_num = j
            if end_num > start_num > 0:
                # print('YES')
                for i in range(start_num + 1, end_num + 1):
                    words[start_num] = words[start_num] + ' ' + words[i]
                    pop_numbers.append(i)
    b = len(pop_numbers)
    while b > 0:
        q = pop_numbers[-k]
        words.pop(q)
        k += 1
        b -= 1

    return 0


def l_param_glue(words: list[str], l_param: str):
    pop_numbers = []
    start_num = 0
    k = 1
    if l_param == '-l':
        for j, word in enumerate(words):
            # print(word)
            if word.startswith('-'):
                start_num = j
            if word.endswith(':') and j > start_num:
                end_num = j
                if end_num > start_num > 0:
                    # print('YES')
                    for i in range(start_num + 1, end_num + 1):
                        words[start_num] = words[start_num] + ' ' + words[i]
                        pop_numbers.append(i)
    b = len(pop_numbers)
    while b > 0:
        q = pop_numbers[-k]
        words.pop(q)
        k += 1
        b -= 1

    return 0


def divide_substring(words: list[str], n_param: int):
    count = int(n_param)
    n = 1
    print('\n' + f"Substring #{n}")

    for i, word in enumerate(words):
        if count <= (len(word)):
            count = int(n_param)
            n += 1
            print('\n' + f"Substring #{n}")
            print(word, end=' ')
            i -= 1
            count = count - len(word) - 1
        else:

            if word == '\n':
                count = count - len(word)
            else:
                count = count - len(word) - 1
            print(word, end=' ')
            i += 1
    return 0


def main(args: list[str]) -> int:
    f_param = '\0'
    n_param = 0
    l_param = '\0'
    for i in range(len(args)):
        if args[i] == "-f":
            print(f"I have -f parameter={args[i + 1]}")
            f_param = args[i + 1]

        if args[i].isdigit() and int(args[i]) > 0:
            print(f"-n parameter is correct={args[i]}")
            n_param = args[i]

        if args[i] == "-l":
            print(f"I have -l parameter={args[i]}")
            l_param = args[i]
    with open(f_param, "rt", encoding="utf-8") as file:
        text = file.read()
        array_by_word = re.findall(r'[^ \n]+|\n', text)

    glue_nickname(array_by_word)
    l_param_glue(array_by_word, l_param)
    divide_substring(array_by_word, int(n_param))

    print(array_by_word)
    # file.close()
    print('\n\n')
    return 0


if __name__ == '__main__':
    main(sys.argv)

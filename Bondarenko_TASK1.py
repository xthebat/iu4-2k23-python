# Bondarenko UI4-82B

import sys


def glue_nickname(file):
    pop_numbers = []
    b = 0
    k = 1
    for j in range(len(file)):
        if file[j][0:1] == "@":
            file[j] = file[j] + ' ' + file[j + 1]
            pop_numbers.append(j + 1)
            b += 1
    while b > 0:
        # array_by_word.pop(pop_numbers[1 - k])
        q = pop_numbers[0 - k]
        file.pop(q)
        # print(pop_numbers[0 - k])
        k += 1
        b = b - 1

    return file


def main(args: list[str]) -> int:

    if args[1] == "-f":
        print(f"I have -f parameter={args[2]}")
    else:
        print("I have not -f parameter")

    if args[4].isdigit() and int(args[4]) > 0:
        print("-n parameter is correct")
    else:
        print('So sad, incorrect -n  parameter')
        exit()

    # if file.isfile('./input_file.txt'):
    file = open(args[2], "rt", encoding="utf-8")
    # else:
    #     print('So sad, so sad')

    text = file.read()
    # считали файл

    import re
    array_by_word = re.findall(r'[^ \n]+|\n', text)

    n = 1
    count = int(args[4])
    glue_nickname(array_by_word)
    # print(array_by_word)

    print('\n' + "Substring #" + str(n))
    for i in range(len(array_by_word)):
        # i - кол слов
        if count <= (len(array_by_word[i])):
            count = int(args[4])
            n += 1
            print('\n' + "Substring #" + str(n))
            print(array_by_word[i], end=' ')
            i = i - 1
            count = count - len(array_by_word[i]) - 1
        else:

            if array_by_word[i] == '\n':
                count = count - len(array_by_word[i])
            else:
                count = count - len(array_by_word[i]) - 1
            print(array_by_word[i], end=' ')
            i += 1

    file.close()
    print('\n\n')
    return 0


if __name__ == '__main__':
    main(sys.argv)

# Bondarenko UI4-82B

import sys


def main(args: list[str]) -> int:
    file_path = args[2] if args[1] == "-f" else None

    if args[1] == "-f":
        print(f"I have -f parameter={args[2]}")
    else:
        print("I have not -f parameter")

    file = open(args[2], "rt", encoding="utf-8")

    count = 0
    text = file.read()
    # считали файл

    array_by_lines = text.split('\n')
    array_by_word = text.split(' ')

    str1 = array_by_lines[0]
    str3 = array_by_lines[-1]

    array2 = []

    n = 1
    count = int(args[4])
    print(count)
    pop_numbers = []
    b = 0
    k = len(array_by_word)
    # 11 - @
    # 12 - name
    for j in range(len(array_by_word)):
        if array_by_word[j][0:1] == "@":
            array_by_word[j] = array_by_word[j] + ' ' + array_by_word[j + 1]
            pop_numbers.append(j + 1)
            b += 1
            # array_by_word.pop(j + 1)
            # j = j - 1
    # взяли -n
    # print(pop_numbers)
    k = 1
    while b > 0:
        # array_by_word.pop(pop_numbers[1 - k])
        q = pop_numbers[0 - k]
        array_by_word.pop(q)
        # print(pop_numbers[0 - k])
        k += 1
        b = b - 1
        # print(array_by_word.pop(q))

    # print(array_by_word)
    print('\n' + "Substring #" + str(n))
    i = 0
    # print(str1)
    # print(array_by_word[13])
    # count = count - len(str1)
    for i in range(len(array_by_word)):
        # i - кол слов
        if count <= (len(array_by_word[i]) + 1):
            count = int(args[4])
            n += 1
            print('\n' + "Substring #" + str(n))
            # i = i - 1

            # if array_by_word[i-1][0:1] == '@':
            #     i = i - 1


            print(array_by_word[i], end= ' ')
            # print(' here ')
            i = i - 1
            # i = i + 1
            count = count - len(array_by_word[i + 1]) - 1
            # i = i -1
            # print(count)

            # # print(text.split(' ')[0:i])
            # выводим сабстринг на каждые -n
        else:


            count = count - len(array_by_word[i]) - 1

            # if array_by_word[i-1][0:1] == '@':
            #     i = i - 1

            print(array_by_word[i], end=' ')
            # print(count)
            i += i
                # print(i)

    # print("NEW", end='\n\n\n\n\n\n\n\n')
    # count = int(args[4])
    # n = 1
    # while i <= len(text):
    #     if count <= 0:
    #         count = int(args[4])
    #         n += 1
    #         print("Substring " + str(n))
    #     else:
    #         count = count - array2[i].length_name() - array2[i].length_score()
    #         i += 1

    # на каком слове сплитить

    # print(array)

    # print(text[0:200])
    file.close()
    #
    # print("WAT", end='\n\n')
    # print(array2)
    # print(array_by_word[12])
    # print(len(array2))
    # print(len(array_by_word))
    # print(array_by_word)
    # print(len(array_by_word[3]))
    # print(len(array_by_word[7]))
    # print(array_by_word[11][0:1])
    if count - len(str3) <= 0:
        print('Substring ' + str(n + 1))
    # print(str3)

    # print('Scoreboard взял отсюда: https://discord.com/channels/690164243685048457/806462228207239179/941307720076783686')

    return 0


if __name__ == '__main__':
    main(sys.argv)

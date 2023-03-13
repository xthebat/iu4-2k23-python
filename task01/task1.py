import argparse
from os import path


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", type=str, required=True)
    parser.add_argument("-n", type=int, required=False, default=200)

    return vars(parser.parse_args())


def smash(text_word, n):
    left = 0
    right = n

    result = []

    if n >= len(text_word):
        result.append(text_word)
        return result

    while True:
        if right >= len(text_word):
            result.append(text_word[left:])
            break
        text_part = text_word[left:right]

        if text_part == '':
            return result

        if text_part[-1] != ' ' and text_part[-1] != '\t' and text_part[-1] != '\n' and \
                text_word[right] != ' ' and text_word[right] != '\t' and text_word[right] != '\n':
            start_word_index = 0
            for i in reversed(range(len(text_part))):
                if text_part[i] == ' ' or text_part[i] == '\t' or text_part[i] == '\n':
                    start_word_index = left + i + 1
                    break
            end_word_index = 0
            for i in range(start_word_index, len(text_word)):
                if text_word[i] == ' ' or text_word[i] == '\t' or text_word[i] == '\n':
                    end_word_index = i
                    break
            if end_word_index >= right and left != start_word_index:
                right = start_word_index
            text_part = text_word[left:right]

        result.append(text_part)
        left = right
        right = left + n
    return result


def main():
    arguments = parse_arguments()
    n = arguments['n']
    file_path = arguments['f']
    if n < 1:
        print("Количество символов в подстроке должно быть больше 0")
        exit(0)
    if not path.exists(file_path):
        print("Некоректный путь к файлу")
        exit(0)
    with open(file_path, "r", encoding="utf-8") as file:
        text_data = file.read()

    text_parts = smash(text_data, n)

    k = 1
    for part in text_parts:
        print(f"Substring #{k}", part, sep='\n')
        k += 1


if __name__ == "__main__":
    main()

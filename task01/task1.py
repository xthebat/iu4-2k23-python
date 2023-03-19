import argparse
from os import path


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", type=str, required=False, default=r"C:\Users\USER\Desktop\Program\python_prrojects\DZ_MLNI\text.txt")
    parser.add_argument("-n", type=int, required=False, default=200)

    return vars(parser.parse_args())


def split_the_string(text_words:str, n:int):
    left = 0
    right = n

    result = []

    if n >= len(text_words):
        result.append(text_words)
        return result

    while True:
        if right >= len(text_words):
            result.append(text_words[left:])
            break
        text_part = text_words[left:right]

        if text_part == '':
            return result

        if text_part[-1] != ' ' and text_part[-1] != '\t' and text_part[-1] != '\n' and \
                text_words[right] != ' ' and text_words[right] != '\t' and text_words[right] != '\n':
            start_words_index = 0
            for i in reversed(range(len(text_part))):
                if text_part[i] == ' ' or text_part[i] == '\t' or text_part[i] == '\n':
                    start_words_index = left + i + 1
                    break
            end_words_index = 0
            for i in range(start_words_index, len(text_words)):
                if text_words[i] == ' ' or text_words[i] == '\t' or text_words[i] == '\n':
                    end_words_index = i
                    break
            if end_words_index >= right and left != start_words_index:
                right = start_words_index
            text_part = text_words[left:right]

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

    text_parts = split_the_string(text_data, n)
    
    k = 1
    for part in text_parts:
        print(f"Substring #{k}", part, sep='\n')
        k += 1


if __name__ == "__main__":
    main()
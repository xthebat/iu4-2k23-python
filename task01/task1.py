import argparse
from os import path


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", type=str, required=False, default=r"C:\Users\USER\Desktop\Program\python_prrojects\DZ_MLNI\text.txt")
    parser.add_argument("-n", type=int, required=False, default=200)

    return vars(parser.parse_args())


def split_the_string(text:str, part_length:int):
    left = 0
    right = part_length

    result = []

    if part_length >= len(text):
        result.append(text)
        return result

    while True:
        if right >= len(text):
            result.append(text[left:])
            break
        text_part = text[left:right]

        if text_part == '':
            return result

        if not text_part[-1].isspace() and not text[right].isspace():
            start_words_index = 0
            for i in reversed(range(len(text_part))):
                if text_part[i].isspace():
                    start_words_index = left + i + 1
                    break
            end_words_index = 0
            for i in range(start_words_index, len(text)):
                if text[i].isspace():
                    end_words_index = i
                    break
            if end_words_index >= right and left != start_words_index:
                right = start_words_index
            text_part = text[left:right]

        result.append(text_part)
        left = right
        right = left + part_length
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
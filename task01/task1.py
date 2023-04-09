import argparse
from os import path


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", type=str, required=True)
    parser.add_argument("-n", type=int, required=False, default=200)

    return vars(parser.parse_args())


def get_tag_indexes(text:str, start=0, end=None):
    if end == None:
        end = len(text)
    start_tag = text.rfind('@', start, end)
    if start_tag != -1:

        space_was_found = False
        for i in range(start_tag, len(text)):
            if text[i] == ':':
                return start_tag, i
            if text[i] == ' ' and not space_was_found:
                space_was_found = True
                continue
            if text[i].isspace() and text[i] != ' ':
                return start_tag, i - 1
            if text[i].isspace() and space_was_found:
                return start_tag, i - 1
        return start_tag, end
    return 0, 0


def split_the_string(text:str, part_length:int):
    left = 0
    right = part_length

    if part_length >= len(text):
        yield text

    while True:
        if right >= len(text):
            yield text[left:]
            break

        text_part = text[left:right]

        if text_part == '':
            break
        
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
            if end_words_index >= right: 
                right = start_words_index
            text_part = text[left:right]

            start_tag, end_tag = get_tag_indexes(text, left, right)
            
            if end_tag > right:
                right = start_tag
                text_part = text[left:right]

        left = right
        right = left + part_length
        yield text_part


def main():
    arguments = parse_arguments()
    n = arguments['n']
    file_path = arguments['f']
    if n < 1:
        raise ValueError("Количество символов в подстроке должно быть больше 0")
    if not path.exists(file_path):
        raise FileNotFoundError("Некоректный путь к файлу")
    with open(file_path, "r", encoding="utf-8") as file:
        text_data = file.read()

    text_parts = split_the_string(text_data, n)
    
    
    for k, part in enumerate(split_the_string(text_data, n), 1):

        print(f"Substring #{k}", part, sep='\n')


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e.args[0])
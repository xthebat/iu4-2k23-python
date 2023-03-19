import argparse
from os import path


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", type=str, required=True)
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
            if end_words_index >= right: 
                right = start_words_index
            text_part = text[left:right]

        start_tag = text.rfind('@', left, right)
        end_tag = 0
        if start_tag != -1:

            space_was_found = False
            for i in range(start_tag, len(text)):
                if text[i] == ':':
                    end_tag = i + 1
                    break
                if text[i] == ' ' and not space_was_found:
                    space_was_found = True
                    continue
                if text[i].isspace() and text[i] != ' ':
                    end_tag = i
                    break
                if text[i].isspace() and space_was_found:
                    end_tag = i
                    break
            
            if end_tag > right:
                right = start_tag
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
        raise ValueError("Количество символов в подстроке должно быть больше 0")
    if not path.exists(file_path):
        raise FileNotFoundError("Некоректный путь к файлу")
    with open(file_path, "r", encoding="utf-8") as file:
        text_data = file.read()

    text_parts = split_the_string(text_data, n)
    
    
    for k, part in enumerate(text_parts, 1):
        print(f"Substring #{k}", part, sep='\n')


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e.args[0])
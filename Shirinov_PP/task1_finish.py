import re
import argparse

def prove_len(str_input: str, lng: int) -> bool:
    lst = str_input.split()
    wmax = len(max(lst, key=len))
    return wmax <= lng

def tag(input_string: str) -> str:
    changed_string = ""
    point = False
    for i, symb in enumerate(input_string):
        if symb == '@':
            point = True
        elif symb == ':':
            point = False
        if symb == ' ' and point:
            changed_string += '*'
        else:
            changed_string += symb
    return changed_string

def privet_substrings(substring_list: list):
    for i, substring in enumerate(substring_list):
        new_substring = substring.replace('*', ' ')
        print(f"Substring {i+1}: {new_substring}")

def split_string(input_string : str, max_length : int) -> list:
    if len(input_string) <= max_length:
        return [input_string]

    substrings = []
    start_index = 0

    while start_index < len(input_string):
        end_index = start_index + max_length

        if end_index < len(input_string) and not input_string[end_index].isspace() and not input_string[end_index-1].isspace():
            near_space = input_string.find(" ", end_index)
            if near_space == -1:
                near_space = len(input_string)

            last_space = input_string.rfind(" ", start_index, end_index)
            end_index = last_space

        if re.search(r'@\s*:', input_string[start_index:end_index]):
            next_index = input_string.find(':', start_index, end_index)
            substrings.append(input_string[start_index:next_index+1])
            start_index = next_index + 1
        elif 'http' in input_string[start_index:end_index]:
            next_index = input_string.find('http', start_index, end_index)
            if next_index != start_index:
                substrings.append(input_string[start_index:next_index])
            next_space = input_string.find(' ', next_index, end_index)
            if next_space == -1:
                next_space = len(input_string)
            substrings.append(input_string[next_index:next_space])
            start_index = next_space
        elif re.search(r'@.+?:', input_string[start_index:end_index]):
            nearest_at_symbol = input_string.rfind('@', start_index, end_index)
            nearest_colon_symbol = input_string.rfind(':', start_index, end_index)
            if nearest_at_symbol > nearest_colon_symbol:
                end_index = nearest_at_symbol
            else:
                end_index = nearest_colon_symbol + 1
            substrings.append(input_string[start_index:end_index])
            start_index = end_index
        else:
            substrings.append(input_string[start_index:end_index])
            start_index = end_index

    if len(substrings) == 1 and substrings[0] == input_string:
        raise ValueError('Error: Could not split input string')
    else:
        return substrings


def print_substrings(substrings:str):
    for i, substring in enumerate(substrings):
        print(f"Substring {i+1}: {substring}")


def main():
        parser = argparse.ArgumentParser()
        parser.add_argument("-f", "--file", help="Path to input file", required=True)
        parser.add_argument("-n", "--max-length", help="Maximum length of substring", type=int, default=200)
        args = parser.parse_args()

        with open(args.file, "r", encoding="utf-8") as f:
            input_string = f.read()

        if prove_len(input_string, args.max_length):
            changed_string = tag(input_string)
            substrings = split_string(changed_string, args.max_length)
            privet_substrings(substrings)
        elif not prove_len(input_string, args.max_length):
            print(f"Маленькое значение для разбиения")


if __name__ == "__main__":
    main()
import sys


def read_file(input_file: str) -> str:
    try:
        with open(input_file, 'r', encoding="utf-8") as f:
            input_string = f.read()
        return input_string
    except FileNotFoundError:
        print("ERROR: Input file not found.")
        sys.exit()


def find_tags(input_string: str) -> str:
    changed_string = ""
    tag_flag = False
    for i, symbol in enumerate(input_string):
        if symbol == '@':
            tag_flag = True
        elif symbol == ':':
            tag_flag = False
        if symbol == ' ' and tag_flag:
            changed_string += '$'
        else:
            changed_string += symbol
    return changed_string


def split_strings(input_string: str, max_length: int = 200) -> list:
    substring_list = []
    current_substring = []
    flag_link = False
    for i, symbol in enumerate(input_string):
        if symbol == " " and not flag_link:
            if len(current_substring) + 1 <= max_length:
                current_substring.append(" ")
            else:
                substring_list.append("".join(current_substring))
                current_substring.clear()
        elif symbol == "\n" and flag_link:
            flag_link = False

        elif symbol == "http" and input_string[i:i+4] == "http":
            if len(current_substring) > 0:
                last_symbol = current_substring[-1]
                if last_symbol != " " and last_symbol != "\n":
                    substring_list.append("".join(current_substring))
                    current_substring.clear()
            flag_link = True
            current_substring.append(symbol)
        elif flag_link:
            current_substring.append(symbol)
        else:
            current_substring.append(symbol)
    if len(current_substring) > 0:
        substring_list.append("".join(current_substring))
    return substring_list


def check_word_length(changed_string: str, max_length: int) -> bool:
    check = False
    word = changed_string.split()
    word_length = len(max(word, key=len))
    if word_length <= max_length:
        check = True
    return check


def output_result(substring_list: list):
    for i, substring in enumerate(substring_list):
        new_substring = substring.replace('$', ' ')
        print(f"Substring {i+1}: {new_substring}")


def main():
    input_file = None
    max_length = 200
    
    for i, arg_key in enumerate(sys.argv):
        if arg_key.find('-f') != -1:
            input_file = sys.argv[i+1]
        if arg_key.find('-n') != -1:
            max_length = int(sys.argv[i+1])

    if input_file is None:
        print("ERROR: Input file path is not specified.")
        sys.exit()

    input_string = read_file(input_file)
    changed_string = find_tags(input_string)
    if check_word_length(changed_string, max_length):
        substring_list = split_strings(changed_string, max_length)
        output_result(substring_list)
    else:
        print('ERROR: Unable to split strings. Try to increase -n parameter')


if __name__ == "__main__":
    main()

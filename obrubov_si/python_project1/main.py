import sys
import os.path
import re
import click


@click.command()
@click.option("-n", "subst_length", default=200, help="Max symbols in substring")
@click.option("-f", "file_path", required=True, help="Max symbols in substring")
def main(subst_length: int, file_path: str):

    if not os.path.isfile(file_path):
        print("incorrect file path")
        return -1

    file = open(file_path, encoding='utf-8')
    text = file.read()
    file.close()
    listed_text = re.findall(r'\S+|\n', text)
    text_with_logins = login_detector(listed_text)
    list_to_print = string_divider(text_with_logins, subst_length)
    output(list_to_print)


def login_detector(input_list: list[str]) -> list[str]:
    output_list = []
    for i in range(len(input_list)):
        if input_list[i].startswith('@') and input_list[i + 1].endswith(':'):
            input_list[i + 1] = input_list[i] + ' ' + input_list[i + 1]
        else:
            output_list.append(input_list[i])
    return output_list


def string_divider(listed_string: list[str], max_length: int) -> list[str]:
    string_length = 0
    string = []
    sorted_text = []
    for i in range(len(listed_string)):
        element_length = 0 if listed_string[i] == '\n' else len(listed_string[i])

        if string_length + element_length + len(string) - string.count('\n') <= max_length:
            string_length += element_length
            if len(string) > 0:
                string_length += 1
            string.append(listed_string[i])
        else:
            if string_length > 0:
                list_to_string = ' '.join(string)
                sorted_text.append(list_to_string)
            string_length = 0
            string = [listed_string[i]]
            string_length += element_length

    if string:
        list_to_string = ' '.join(string)
        sorted_text.append(list_to_string)

    return sorted_text


def output(sorted_text: list[str]):
    for i in range(len(sorted_text)):
        print(f"\nSubstring #{i + 1}:\n{sorted_text[i]}")


if __name__ == '__main__':
    main(sys.argv)

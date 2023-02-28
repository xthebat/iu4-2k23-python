import argparse
import os
import pathlib


def main(par):
    check_path(par.file)
    text = read_file(par.file)
    dog_list = find_all_dogs(text)
    flag, result_list = divide_string(text, dog_list, par.number)
    result(flag, result_list)


def check_path(path):
    file = pathlib.Path(path)
    if not file.is_file():
        print("No such file")
        exit(0)
    if not os.stat(path).st_size:
        print("File is empty")
        exit(0)


def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()
    return text + " "


def find_all_dogs(text):
    dog_list = []
    final_dog_list = []
    flag = False
    for i in range(len(text)):
        if text[i] == "@":
            flag = True
            dog_list.append(i)
        if flag is True and text[i] == ":":
            dog_list.append(i)
            flag = False
    for i in range(1, len(dog_list), 2):
        final_dog_list.append((dog_list[i - 1], dog_list[i]))
    return final_dog_list


def divide_string(text, dog_list, number):
    result_list = []
    start_index = 0
    error_string = False

    while start_index < len(text) - 1:
        end = start_index + number
        if end > len(text):
            end = len(text) - 1
        if (text[end] == " " or text[end] == "\n") and check_between(end, dog_list):
            result_list.append(text[start_index:end + 1])
            start_index = end + 1
        else:
            stop = False
            while not stop:
                end = text.rfind(" ", start_index, end)
                if end == -1:
                    stop = True
                    error_string = True
                    start_index = len(text)  # to exit 'while' immediately
                else:
                    if check_between(end, dog_list):
                        result_list.append(text[start_index:end + 1])
                        start_index = end + 1
                        stop = True

    return error_string, result_list


def check_between(end, dog_list):
    norm = True
    for k in dog_list:
        if k[0] < end < k[1]:
            norm = False
            break
    return norm


def result(flag, result_list):
    if not flag:
        for i, string in enumerate(result_list):
            print(f"Substring {i + 1}:\n{string}\n")
    else:
        print("Error in dividing substring")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Enter arguments")
    parser.add_argument('-n', '--number', type=int, default=200, help="Enter '-n' to set number of symvols i")
    parser.add_argument('-f', '--file', type=str, help="Enter path to file works only with '-f' in front")
    args = parser.parse_args()
    main(args)

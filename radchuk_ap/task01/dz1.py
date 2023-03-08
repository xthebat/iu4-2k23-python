import os
import sys

def error(msg, code):
	print(msg)
	exit(code)

def check_if_next_exist(arguments, i, msg):
	if i + 1 >= len(arguments):
		error(msg, 0)

def check_input():
	input_file_name = output_file_path = None
	max_symbols = 200
	is_indivisible_string = False
	filter_function = "lambda r: True" 

	for i in range(len(sys.argv)):
		match sys.argv[i]:
			case '-f':
				check_if_next_exist(sys.argv, i, "После ключа -f должен идти путь к файлу!")
				input_file_name = sys.argv[i + 1]
			case '-n':
				check_if_next_exist(sys.argv, i, "После ключа -n должен идти положительный целочисленный аргумент!")
				try: max_symbols = int(sys.argv[i + 1])
				except: error("Для ключа -n должно вводиться натуральное число!", 0)
			case '-l': # Bonus 1
				is_indivisible_string = True
			case '-d': # Bonus 2
				check_if_next_exist(sys.argv, i, "После ключа -d должна указываться директория!")
				output_file_path = sys.argv[i + 1]
			case '-r': # Hardcore
				check_if_next_exist(sys.argv, i, "После ключа -r должна быть написана булева лямбда-функция!")
				filter_function = sys.argv[i + 1]
			case _: 
				pass

	if not os.path.exists(input_file_name):
		error("Данного файла не существует!", 0)

	if (output_file_path is not None) and (not os.path.exists(output_file_path)):
		error("Данного файла не существует!", 0)

	return input_file_name, max_symbols, is_indivisible_string, output_file_path, filter_function

def save_append(lst, substring_lst, max_symbols):
	elem = ' '.join(substring_lst)

	if len(elem) > max_symbols:
		error(f"Текст не может быть разбит на строки по {max_symbols} символов!", 0)

	lst.append(elem)

def split_by_conditions(i, is_indivisible_string):
	if is_indivisible_string and i[0] == '-':
		return [i]

	list_of_words = i.split(' ')
	iterator = 0
	result = []

	while iterator < len(list_of_words):
		if list_of_words[iterator][0] == '@':
			result.append(list_of_words[iterator] + ' ' + list_of_words[iterator + 1])
			iterator += 1
		else:
			result.append(list_of_words[iterator])
		iterator += 1

	return result

def parse_string(list_of_words, cosib, substring_lst, substrings, max_symbols):
	for word in list_of_words:				
		is_begin = bool(len(substring_lst))

		if cosib + len(word) + is_begin <= max_symbols:
			substring_lst.append(word)
			cosib += len(word) + is_begin
		else:
			save_append(substrings, substring_lst, max_symbols)
			substring_lst = [word]
			cosib = len(word)

	return cosib, substring_lst, substrings, max_symbols


def parse(file_path, max_symbols, is_indivisible_string, filter_function):
	substrings = []

	l_f = eval(filter_function)
	substring_lst = []
	cosib = 0 # count_of_symbols_in_buffer

	with open(file_path, encoding='utf-8') as file:
		for string in file:

			if not l_f(string): # Если условие не выполняется, то строка пропускается
				continue
			
			list_of_words = split_by_conditions(string, is_indivisible_string)
			cosib, substring_lst, substrings, max_symbols = parse_string(list_of_words, cosib, substring_lst, substrings, max_symbols)

	if len(substring_lst):
		save_append(substrings, substring_lst, max_symbols)

	return substrings


def print_in_file(lst, output_file_path):
	for i in range(len(lst)):
		file_name = f"{output_file_path}substring_{i+1}.txt"

		with open(file_name, 'w+', encoding='utf-8') as file:
			file.write(lst[i])

def print_in_console(lst):
	for i in range(len(lst)):
		print(f"Substring #{i + 1}:\n {lst[i]}")

def print_output(lst, output_file_path):
	if output_file_path is not None:
		print_in_file(lst, output_file_path)
	else:
		print_in_console(lst)


if __name__ == '__main__':

	input_file_name, max_symbols, is_indivisible_string, output_file_path, filter_function = check_input()

	substrings = parse(input_file_name, max_symbols, is_indivisible_string, filter_function)

	print_output(substrings, output_file_path)

import os
import sys

def ERROR(msg, code):
	print(msg)
	exit(0)

def CHECK_INPUT():
	param1 = param4 = None
	param2 = 200
	param3 = False
	param5 = "lambda r: True" 

	for i in range(len(sys.argv)):
		match sys.argv[i]:
			case '-f':
				param1 = sys.argv[i + 1]
			case '-n':
				try: param2 = int(sys.argv[i+1])
				except: ERROR("Для ключа -n должно вводиться натуральное число!", 0)
			case '-l': # Bonus 1
				param3 = True
			case '-d': # Bonus 2
				param4 = sys.argv[i + 1]
			case '-r': # Hardcore
				param5 = sys.argv[i + 1]
			case _: 
				pass

	if not os.path.exists(param1):
		ERROR("Данного файла не существует!", 0)

	if param4 != None and not os.path.exists(param4):
		ERROR("Данного файла не существует!", 0)

	return param1, param2, param3, param4, param5

def save_append(lst, elem, MAX_SYMBOLS):
	if len(elem) > MAX_SYMBOLS:
		ERROR(f"Текст не может быть разбит на строки по {MAX_SYMBOLS} символов!", 0)
	lst.append(elem)

def PARSE(FILE_PATH, MAX_SYMBOLS, IS_L_PARAM, IS_R_PARAM):
	substrings = []

	l_f = eval(IS_R_PARAM)

	with open(FILE_PATH, encoding='utf-8') as file:
		substring = ""

		for i in file:

			if not l_f(i): # Если условие не выполняется, то строка пропускается
				continue

			list_of_words = i.split(' ')
			new_list_of_words = []

			if IS_L_PARAM and i[0] == '-':
				new_list_of_words = [i]
			else:
				iterator = 0
				while iterator < len(list_of_words):
					if list_of_words[iterator][0] == '@':
						new_list_of_words.append(list_of_words[iterator] + ' ' + list_of_words[iterator + 1])
						iterator += 1
					else:
						new_list_of_words.append(list_of_words[iterator])
					iterator += 1

			for j in range(len(new_list_of_words)):
				
				is_begin = [' ', 1] if len(substring) != 0 else ['', 0]

				if len(substring) + len(new_list_of_words[j]) + is_begin[1] <= MAX_SYMBOLS:
					substring += is_begin[0] + new_list_of_words[j]
				else:
					save_append(substrings, substring, MAX_SYMBOLS)
					substring = new_list_of_words[j]

		if len(substring) != 0:
			save_append(substrings, substring, MAX_SYMBOLS)

	return substrings
	

def PRINT_OUTPUT(lst, is_d_param):
	if is_d_param != None:
		for i in range(len(lst)):
			file_name = is_d_param + f"substring_{i+1}.txt"

			with open(file_name, 'w+', encoding='utf-8') as file:
				file.write(lst[i])
	else:
		for i in range(len(lst)):
			print(f"Substring #{i + 1}:")
			print(lst[i])


if __name__ == '__main__':

	FILE_PATH, MAX_SYMBOLS, IS_L_PARAM, IS_D_PARAM, IS_R_PARAM = CHECK_INPUT()
	# print(FILE_PATH, MAX_SYMBOLS, IS_L_PARAM, IS_D_PARAM, IS_R_PARAM)
	SUBSTRINGS = PARSE(FILE_PATH, MAX_SYMBOLS, IS_L_PARAM, IS_R_PARAM)

	PRINT_OUTPUT(SUBSTRINGS, IS_D_PARAM)
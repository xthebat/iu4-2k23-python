import sys
import os

def sort_string(TEXT, MAX_INDEX, START_INDEX, INDEX_INC, L_RULE,D_RULE, FILE_CNT):
    CNT = START_INDEX
    END_INDEX = -1
    TEXT_LENGTH = len(TEXT)
    if CNT == TEXT_LENGTH + 1:
        print('Строки разделены')
        quit()
    if TEXT_LENGTH - CNT < INDEX_INC:
            print_string(TEXT_LENGTH, MAX_INDEX, TEXT, START_INDEX, INDEX_INC, L_RULE, D_RULE, FILE_CNT)
    while ((CNT <= MAX_INDEX) and CNT != TEXT_LENGTH):
        if TEXT[CNT] == '@':
            CNT_SAVE = CNT
            temp = TEXT.find(':', CNT, TEXT_LENGTH - 1)
            if temp < (MAX_INDEX - 1) and temp != -1:
                CNT = temp + 1
                if (L_RULE == 1):
                    CNT += 1
                    while TEXT[CNT].isnumeric() == 1:
                        CNT += 1
                        if TEXT[CNT] == TEXT[-1]:
                            break
                    if CNT >= MAX_INDEX and END_INDEX == -1:
                        print('Невозможно разделить следующую строку ')
                        quit()
                    if CNT >= MAX_INDEX:
                        CNT = CNT_SAVE + 1
            elif temp == -1:
                CNT += 1
            elif END_INDEX == -1:
                print('Невозможно разделить следующую строку ')
                quit()
            else:
                print_string(END_INDEX, MAX_INDEX, TEXT, START_INDEX, INDEX_INC, L_RULE, D_RULE, FILE_CNT)

        if TEXT[CNT] == ' ':
            END_INDEX = CNT
            if CNT - 1 < MAX_INDEX:
                CNT += 1
        elif TEXT[CNT] == '\n':
            END_INDEX = CNT
            if CNT - 1 < MAX_INDEX:
                CNT += 1
        else:
            CNT += 1
    if END_INDEX == -1:
        print('Невозможно разделить строку')
        quit()
    print_string(END_INDEX, MAX_INDEX, TEXT, START_INDEX, INDEX_INC, L_RULE, D_RULE, FILE_CNT)

def print_string(END_INDEX, MAX_INDEX, TEXT, START_INDEX, INDEX_INC, L_RULE, D_RULE, FILE_CNT):
    FINAL_STR = TEXT[START_INDEX:END_INDEX]
    if D_RULE == 1:
        # NEW_FILE = open(fr"{sys.argv[7]}\STR{FILE_CNT}.txt", "w+")
        # NEW_FILE.write(FINAL_STR)
        # NEW_FILE.close()
        # os.mknod("str" + FILE_CNT + " .txt")
        with open (sys.argv[7] + "str" + str(FILE_CNT) + ".txt", "w") as NEW_FILE:
            NEW_FILE.write("%s" % FINAL_STR)
        # with open('str'+FILE_CNT+' .txt', 'w') as f:
        #     f.write("%s\n" % FINAL_STR)
        # NEW_FILE = os.path.join(f"{sys.argv[7]}", f'str{FILE_CNT}.txt')
        # print(FINAL_STR, NEW_FILE)
        FILE_CNT += 1
    print(FINAL_STR)
    # print('\n')
    START_INDEX = END_INDEX + 1
    MAX_INDEX = START_INDEX + INDEX_INC
    sort_string(TEXT, MAX_INDEX, START_INDEX, INDEX_INC, L_RULE, D_RULE, FILE_CNT)

def main(args: list[str]):
    L_RULE = 0
    D_RULE = 0
    print('Введите -f "путь к файлу" -n "Максимальное количество символов"')
    if len(sys.argv) == 1:
         print('Введите -f "путь к файлу" -n "Максимальное количество символов"')
         # Нужно вернуться к началу выполнения функции
    else:
        PARAM_NAME = sys.argv[1]
    if PARAM_NAME == '-f':
        FILE_PATH = sys.argv[2]
    else:
        print(f'Неизвесный параметр {PARAM_NAME}')
        quit()
    PARAM_NAME = sys.argv[3]
    if PARAM_NAME == '-n':
        MAX_INDEX = int(sys.argv[4]) + 1
    else:
        print(f'Неизвесный параметр {PARAM_NAME}')
        quit()
    if len(sys.argv) > 4:
        PARAM_NAME = sys.argv[5]
        if PARAM_NAME == '-l':
            L_RULE = 1
        else:
            print(f'Неизвесный параметр {PARAM_NAME}')
            quit()
    if len(sys.argv) > 5:
        PARAM_NAME = sys.argv[6]
        if PARAM_NAME == '-d':
            D_RULE = 1
            # FILE_PATH = f"{sys.argv[7]}"
            # os.mkdir(FILE_PATH, mode=0o777)
        else:
            print(f'Неизвесный параметр {PARAM_NAME}')
            quit()

    INDEX_INC = MAX_INDEX
    FILE_CNT = 1

    file = open(sys.argv[2])
    TEXT = file.read()
    START_INDEX = 0
    sort_string(TEXT, MAX_INDEX, START_INDEX, INDEX_INC, L_RULE, D_RULE, FILE_CNT)

if __name__=='__main__':
    main(sys.argv)
import sys
import os.path

# Функция разбиения на подстроки
def divide(filename: str, lenght: int) -> list[str]:
    massive = []
    string = []
    file = open(filename, encoding='utf-8')
    pos = 0
    ind = True
    startpos = 0
    endflag = 0
    lrule = 0
    text = file.read()
    file.close()
    while (ind != False):
        if endflag == 0:
            while lenght > len(text[startpos:pos]):
                if text.find("@", pos) - pos == 1:
                    taglen = text.find(":", pos) - text.find("@", pos)
                    if lenght - len(text[startpos:pos]) > taglen:
                        string = text[startpos:pos]
                    elif lenght - len(text[startpos:pos]) == taglen:
                        pos = text.find(":", lastpos)
                        string = text[startpos:pos]
                        break
                    else:
                        string = text[startpos:pos]
                        break
                elif text.find(" ", pos) == -1:
                    endflag = 1
                    break
                else:
                    string = text[startpos:pos]
                lastpos = pos
                pos = text.find(" ", pos + 1)
            pos = lastpos
            startpos = pos
            if len(string) > 0:
                massive.append(string)
                string = []
        else:
            string = text[pos + 1:len(text)]
            massive.append(string)
            ind = False
            string = []
            endflag = 0
            break
    return massive

# Проверка на максимально длинное слово и возможность его вывода
def lencheck(filename: str, lenght: int) -> bool:
    file = open(filename, encoding='utf-8')
    text = file.read()
    lst = text.split()
    wmax = len(max(lst, key=len))
    file.close()
    if wmax <= lenght:
        return True
    else:
        return False

# Функция вывода подстрок
def output(massive: list[str], dcheck: bool, path: str):
    for i in range(len(massive)):
        print(f"\nSubstring #{i + 1}:\n{massive[i]}")
        if dcheck == True:
            file = open(f"{path}\substring_{i + 1}.txt", "w+")
            file.write(f"{massive[i]}")
            file.close()

def main(args: list[str]):

    # Определение наличия аргумента -d
    if len(args) > 3 and (args[3] == "-d" or args[5] == "-d"):
        dflag = True
    else:
        dflag = False

    # Определение наличия аргумента -n
    if len(args) > 3 and args[3] == "-n":
        numb = int(args[4])
    else:
        numb = 200

    if args[1] == "-f" and len(args) >= 3:
        if os.path.isfile(args[2]) and lencheck(args[2], numb) == True:
            outputdate = divide(args[2], numb)
            if args[3] == "-d":
                output(outputdate, dflag, args[4])
            elif args[5] == "-d":
                output(outputdate, dflag, args[6])
            else:
                output(outputdate, dflag)
        elif os.path.isfile(args[2]) and lencheck(args[2], numb) == False:
            print(f"Слишком маленькое значение для разбиения")
        else:
            print(f"Некорректное название файла/директории")
    else:
        print(f"Некорректно введенные данные")

if __name__ == '__main__':
    sys.exit(main(sys.argv))
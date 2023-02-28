import os.path
import sys


def symbCounter(name: str, number: int) -> bool:  # Проверка длины ссылки
    with open(name, encoding='utf-8') as file:
        text = file.read()
        link = text[text.find("http"):len(text)]
        file.close()
    return len(link) <= number  # Если длина ссылки меньше введенного значения, то выводим True


def splitStr(name: str, number: int) -> list[str]:
    mass = []
    file = open(name, encoding='utf-8')
    text = file.read()
    file.close()
    pos = 0
    ind = 0
    prevpos = 0
    i = 0
    pos = text.find(" ", pos)
    fixPos = pos
    link = 0
    sample = text[0:pos]
    while (ind != -1):
        if link == 0:
            while number > len(text[prevpos:pos]):
                if text.find("@", pos) - pos == 1:
                    i = text.index(":", pos) - text.index("@", pos)
                    if number - len(text[prevpos:pos]) > i:
                        sample = text[prevpos:pos]
                    elif number - len(text[prevpos:pos]) == i:
                        pos = text.find(":", pos)
                        sample = text[prevpos:pos]
                        break
                    else:
                        sample = text[prevpos:fixPos]
                        break
                elif text.find("http", pos) - pos == 1:
                    link = 1
                    sample = text[prevpos:pos]
                    break
                else:
                    sample = text[prevpos:pos]
                fixPos = pos
                pos = text.find(" ", pos + 1)
            pos = fixPos
            prevpos = pos
            mass.append(sample)
            sample = []
            pos = fixPos

        else:
            sample = text[text.find("http"):len(text)]
            mass.append(sample)
            ind = -1
            sample = []
            link = 0
            break
    return mass


def output(strings: list[str]):
    for i in range(len(strings)):
        print(f"Substring #{i + 1}:\n{strings[i]}")


def main(args: list[str]):
    if args[1] == "-f" and len(args) == 3:
        if os.path.isfile(args[2]):
            massiv = splitStr(args[2], 200)
            output(massiv)
        else:
            print(f"Вы ввели некорректное название файла или директорию к нему")
    elif args[1] == "-f" and len(args) == 5 and args[3] == "-n":
        if os.path.isfile(args[2]) == True and symbCounter(args[2], int(args[4])) == True:
            massiv = splitStr(args[2], int(args[4]))
            output(massiv)
        elif os.path.isfile(args[2]) == True and symbCounter(args[2], int(args[4])) == False:
            print(f"Вы ввели слишком маленькое значение для разбиения на подстроки")
        else:
            print(f"Вы ввели некорректное название файла или директорию к нему")
    else:
        print(f"Вы ввели некорректный параметр строки")


if __name__ == '__main__':
    sys.exit(main(sys.argv))

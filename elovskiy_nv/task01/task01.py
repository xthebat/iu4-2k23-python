import sys
import os.path


# Открытие и чтение файла
def inputfile(filename: str) -> str:
    with open(filename, encoding='utf-8') as f:
        text = f.read()
    return text


# Проверка на максимально длинное слово и возможность его вывода
def lencheck(text: str, lenght: int) -> bool:
    lst = text.split()
    wmax = len(max(lst, key=len))
    return wmax <= lenght


# Функция разбиения строки на подстроки
def dividestr(text: str, length: int) -> list[str]:
    subline = []
    words = []
    nowpos = startsub = endflag = 0
    while True:
        while length > nowpos - startsub:
            if text.find(" ", nowpos) == -1:
                endflag = 1
                break
            tagstart = text.find("@", nowpos)
            tagend = text.find(":", tagstart)
            taglength = tagend - tagstart
            if tagstart - nowpos == 1 and length - len(words) == taglength:
                words = text[startsub:tagend]
                buff = tagend
                break
            elif tagstart - nowpos == 1 and length - len(words) < taglength:
                break
            words = text[startsub:nowpos]
            buff = nowpos
            nowpos = text.find(" ", nowpos + 1)
        startsub = nowpos = buff
        subline.append(words)
        if endflag:
            words = text[nowpos + 1:-1]
            subline.append(words)
            break
    return subline


# Функция вывода подстрок
def output(subline: list[str], dcheck: bool, path: str):
    for i, word in enumerate(subline):
        print(f"\nSubstring #{i + 1}:\n{word}")
        if dcheck:
            with open(f"{path}substring_{i + 1}.txt", "w+") as f:
                f.write(f"{subline[i]}")
    return 0


def main():
    numb = 200
    dflag = False

    # Определение положения аргументов и их значений
    for i in range(len(sys.argv)):
        match sys.argv[i]:
            case '-f':
                fpath = sys.argv[i + 1]
            case '-n':
                numb = int(sys.argv[i + 1])
            case '-d':
                dflag = True
                dpath = sys.argv[i + 1]

    text = inputfile(fpath)
    if os.path.isfile(fpath) and lencheck(text, numb):
        outputdate = dividestr(text, numb)
        if dflag:
            output(outputdate, dflag, dpath)
        else:
            output(outputdate, dflag)
    elif not lencheck(text, numb):
        print(f"Слишком маленькое значение для разбиения")
    elif not os.path.isfile(fpath):
        print(f"Некорректное название файла/директории")
    else:
        print(f"Некорректно введенные данные")


if __name__ == '__main__':
    sys.exit(main())
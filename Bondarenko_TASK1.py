# Bondarenko UI4-82B

import sys


class Chel:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def length(self):
        return len(self.name) + len(self.score) + 1 + len('- Новый score пользователя ')
    # функция для класса для узнования длины всей этой штуки

    def vivod(self):
        return '- Новый score пользователя ' + self.name + ' ' + self.score
    # функция для возвращиния именно стринга


def main(args: list[str]) -> int:

    # if len(args) < 2:
    #     print(f"not enough {len(args)=} requared > 2 ")
    #     return -1
    #
    file_path = args[2] if args[1] == "-f" else None
    #
    if args[1] == "-f":
        print(f"I have -f parameter={args[2]}")
    else:
        print("I have not -f parameter")
    #
    # for index, it in enumerate(args):
    #     print(f"args[{index}]={it}")
    # # parametres aquaered
    #
    # print("BEGIN", end='\n\n\n')
    # ЭТА ВСЕ ШТУКА ДЛЯ ПАРАМЕТРОВ
    file = open(args[2], "rt", encoding="utf-8")
    # # print(file.read())
    count = 0
    text = file.read()
    # считали файл
    

    array3 = text.split('\n')
    # чтобы норм вывести первые и последние строки
    str1 = array3[0]
    str3 = array3[-1]
    # последняя строка
    array2 = []
    for k in range(len(array3) - 2):
        array = array3[k + 1].split()
        array2.append(Chel(array[-3] + ' ' + array[-2], array[-1]))
        # объединили name, чтобы не поделить их
    n = 1
    count = int(args[4])
    print("Substring " + str(n))
    print(str1)
    count = count - len(str1)
    for i in range(len(array2)):
        if count <= 0:
            count = int(args[4])
            n += 1
            print("Substring " + str(n))
            # выводим сабстринг на каждые 200
        else:
            print(array2[i].vivod())
            count = count - array2[i].length()



    # на каком слове сплитить

    # print(array)
    
    # print(text[0:200])
    file.close()

    if count - len(str3) <= 0:
        print('Substring ' + str(n + 1))
    print(str3)

    # print('Scoreboard взял отсюда: https://discord.com/channels/690164243685048457/806462228207239179/941307720076783686')

    return 0
if __name__ == '__main__':
    main(sys.argv)
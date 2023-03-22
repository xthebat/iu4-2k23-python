# Stream 05

## Структура проекта в IntelliJ

## Pytest
- requirements.txt
- Полезные ссылки:
  https://pip.pypa.io/en/stable/reference/requirements-file-format/
  https://peps.python.org/pep-0440/#compatible-release
- pytest~=7.2

## Произвольные аргументы
- `*args` 
- `**kwargs`

## Функциональное программирование
- lambda-функция (стратегия)
- предикат

## Декораторы
- nested functions
- logable decorator
- simple_cache decorator

## Параметрические тесты
Полезные ссылки: 
- https://docs.pytest.org/en/6.2.x/parametrize.html

## Коллекции:

### list
Что не забыть рассказать:
- Что он есть...
- clear(), extend(), pop(), append(), insert(), sort(), reverse()
- https://stackoverflow.com/questions/3917574/how-is-pythons-list-implemented

### tuple
Что не забыть рассказать:
- Для чего используется
- Чем отличается list

### set
Что не забыть рассказать:
- Для чего используется
- Уникальные элементы/способы доступа
- Чем отличается tuple и list
- intersection(), difference(), union()

### dict
Что не забыть рассказать:
- Для чего используется
- get(), fromkeys(), setdefault(), items(), keys()
- получить уникальные элементы без изменения порядка

## Comprehension:
- comprehension для list
- comprehension для dict
- поиск (next/get)
- модификация
- фильтрация
- морж-оператор в list-comprehension

## Встроенные функции Python
Полезные ссылки:
- https://docs.python.org/3/library/functions.html

Что не забыть рассказать:
- ленивые вычисления
- sum, max, min
- range, len, enumerate
- map, filter, any, all, sorted, reversed
- zip
- next
- isinstance, issubclass, id, type

~~generator~~
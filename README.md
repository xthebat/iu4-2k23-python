# Stream 06

## Структура проекта в IntelliJ

## Pytest

- Что делают программисты IntelliJ на работе или как пофиксить pytest-benchmark...

## Коллекции:

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
- starmap
- isinstance, issubclass, id, type

## Классы в Python

Терминология ООП - выучить наизусть
https://www.tutorialspoint.com/python/python_classes_objects.htm
Принципы ООП - выучить наизусть
https://tproger.ru/translations/oop-principles-cheatsheet/
https://topjava.ru/blog/oops-concepts-in-java
https://medium.com/nuances-of-programming/%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BD%D0%BE-%D0%BE%D1%80%D0%B8%D0%B5%D0%BD%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%BE%D0%B5-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B4%D0%BB%D1%8F-%D1%81%D0%B0%D0%BC%D1%8B%D1%85-%D0%BC%D0%B0%D0%BB%D0%B5%D0%BD%D1%8C%D0%BA%D0%B8%D1%85-b0e0578761f1
https://skillbox.ru/media/code/kak-izbezhat-putanitsy-v-kode-ili-kratkiy-kurs-oop-na-python/

- Как объявить класс + конструктор
    - public/protected/private члены класса
    - Аксессоры (геттеры и сеттеры)
    - Статические переменные для обычных классов
        - (!) Изменяемые статические переменные
- dataclass'ы - стараемся использовать их
    - наследование
    - особенности инициализации полей (default_factory)
    - параметры создания dataclass (frozen, unsafe_hash)
    - преобразование к словарю и обратно
    - https://docs.python.org/3/library/dataclasses.html
- Как наследовать классы
    - Просто наследование
    - Наследование встроенных типов
    - Интерфейсы, протоколы, ABC
- magic-методы (операторы)
    - __repr__, __str__, __hash__, __eq__, __call__, __iter__, __next__ ...
- staticmethod'ы и classmethod'ы - как создавать классы
- Метаклассы и динамическое создание классов :)

## Как сохранять в JSON
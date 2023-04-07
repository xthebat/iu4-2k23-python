from pathlib import Path
import clang.cindex

#Make by Ilyin

# Инициализация индекса для доступа к API библиотеки libclang
clang.cindex.Config.set_library_file("C:/Program Files/LLVM/bin/libclang.dll")
index = clang.cindex.Index.create()


def parse_file(file_path):
    # Получение абсолютного пути до файла
    file_path = str(file_path.resolve())

    # Создание AST из файла
    tu = index.parse(file_path)

    # Обход AST и вывод информации о каждом узле
    for node in tu.cursor.walk_preorder():
        print(f"Kind: {node.kind}, Spelling: {node.spelling}, Type: {node.type.spelling}")


# Путь до директории с примерами кода
examples_dir = Path("./examples")

# Список файлов для парсинга
files = [
    examples_dir / "example1.c",
    examples_dir / "example2.c",
    examples_dir / "example3.c",
]

# Парсим каждый файл и выводим результат
for file_path in files:
    print(f"--- {file_path.name} ---")
    parse_file(file_path)

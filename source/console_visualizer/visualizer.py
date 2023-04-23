class DataVisualizer:
    def __init__(self, data_: dict):
        self._data = data_

    def print_units(self, type_):
        out_dict = self._data[type_]
        if not out_dict:
            print(f'No accesible data to type "{type_}"\n')
            return

        print(f'Data for type "{type_}":\n')

        for unit in out_dict:
            print(f"Line - {unit['line']}\n"
                  f"Offset - {unit['offset']}")
            for key, value in unit['object'].items():
                if isinstance(value, list):
                    print(f'{key.capitalize()}:')
                    for sub_value in value:
                        print(f'\t{sub_value["name"]}: {sub_value["type"]}')
                    continue
                print(f'{key.capitalize()} - {value}')

            print()

        print()

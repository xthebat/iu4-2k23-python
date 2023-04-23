from json import dumps, loads
from sys import stderr


class Loader(object):
    def __init__(self, dest_path_: str, source_path_=None, is_json=False):
        try:
            with open(dest_path_, 'r'):
                pass
        except FileNotFoundError:
            print(f'[ERROR] Can\'t open file with name <{dest_path_}>!', file=stderr)
            exit(1)
        self._source_path = source_path_ if source_path_ else dest_path_
        self._dest_path = dest_path_

    def read_header_file(self) -> list:
        with open(self._source_path, 'r') as fstream:
            return fstream.readlines()

    def load_data(self) -> dict:
        with open(self._dest_path, 'r') as fstream:
            return loads(fstream.read())

    def dump_data(self, data: dict) -> None:
        with open(self._dest_path, 'w') as fstream:
            fstream.write(dumps(data))

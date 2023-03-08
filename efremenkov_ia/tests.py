import unittest
from main import parse_args, main
import shlex
from main import InputArgumentError, PredicateError
import os


class TestSplitter(unittest.TestCase):

    def _create_subtest_with_args(self, test_cases: list[tuple], assert_method: bool):

        for arg, expected in test_cases:
            with self.subTest(arg=arg, expected=expected):
                execution_args = shlex.split(arg)
                execution_folder = f"{os.path.dirname(os.path.abspath(__file__)) + 'main.py'}"
                execution_args.insert(0, execution_folder)
                if assert_method:
                    self.assertEqual(expected, main(parse_args(execution_args)))
                else:
                    with self.assertRaises(expected):
                        main(parse_args(execution_args))

    def test_asserts(self):
        test_cases = [
            ("-f file.txt -n 200 -r 'lambda line: line.startswith(\"-\")'", None),
            ('-f file.txt -n 100', None),
            ('-f file.txt -n 200 -l -r "lambda line: len(line) == 45"', None),
            ('-f file.txt -n 110 -d foldername', None),
            ('-f file.txt -l', None),
        ]
        self._create_subtest_with_args(test_cases, True)

    def test_raises(self):
        test_cases = [
            ('-f file.txt -n s', InputArgumentError),
            ('-f file.txt -n 0', ValueError),
            ('-f files.txt', FileNotFoundError),
            ('-f file.txt -n 200 -l -r "lambd line: len(line) == 45"', PredicateError)
        ]
        self._create_subtest_with_args(test_cases, False)


if __name__ == "__main__":
    unittest.main()

import unittest
from main import parse_args, main
import shlex
from main import ArgumentError


class TestSplitter(unittest.TestCase):

    def test_main_with_args(self, test_cases: list[tuple], assert_equals: bool):

        for arg, expected in test_cases:
            with self.subTest(arg=arg, expected=expected):
                parsed_args = shlex.split(arg)
                parsed_args.insert(0, "'F:\\python\\iu4-2k23-python\\efremenkov_ia\\main.py'")
                parsed_args = parse_args(parsed_args)
                if assert_equals is True:
                    self.assertEqual(main(parsed_args), expected)
                else:
                    self.assertRaises(expected, main(parsed_args))

    def test_asserts(self):
        test_cases = [
            ("-f file.txt -n 200 -r 'lambda line: line.startswith(\"-\")'", None),
            ('-f file.txt -n 100', None),
            ('-f file.txt -n 200 -l -r "lambda line: len(line) == 45"', None),
            ('-f file.txt -n 110 -d foldername', None),
            ('-f file.txt -l', None),
        ]
        self.test_main_with_args(test_cases, True)

    def test_raises(self):
        test_cases = [
            ('-f file.txt -n s', ArgumentError),
            ('-f file.txt -n 0', ValueError),
            ('-f files.txt', FileNotFoundError)
        ]
        self.test_main_with_args(test_cases, False)


if __name__ == "__main__":
    unittest.main()

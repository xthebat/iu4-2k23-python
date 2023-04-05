from stream05.decorator_sample import loggable


def test_loggable(capsys):
    @loggable
    def test(x: int, y: int):
        return x + y

    test(10, 20)

    captured = capsys.readouterr()

    assert captured.out == "args=(10, 20) result=30\n"

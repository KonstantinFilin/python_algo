from fibo import fibo


def test_fibo():
    assert fibo(-1) == []
    assert fibo(0) == []
    assert fibo(1) == [1]
    assert fibo(2) == [1, 1]
    assert fibo(3) == [1, 1, 2]
    assert fibo(10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


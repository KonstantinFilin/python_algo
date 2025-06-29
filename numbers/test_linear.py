from linear import *


def test_linear():
    assert linear(3, 18) == 6
    assert linear(2, -2) == -1
    assert linear(3, 24) == 8


def test_linear_zeros():
    assert linear_zeros(3, 18) == (6, -18)
    assert linear_zeros(2, -2) == (-1, 2)
    assert linear_zeros(3, 24) == (8, -24)



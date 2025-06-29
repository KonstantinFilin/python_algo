from quadratic import *


def test_quadratic():
    assert quadratic(1, 4, 4) == (0, (-2.0), -2.0)
    assert quadratic(1, 2, -3) == (16, (1, -3), -1)
    assert quadratic(2, 4, 8) == (-48, (), -1)

def test_quadratic2():
    assert quadratic2(1, 4, 4) == (0, (-2.0), -2.0)
    assert quadratic2(1, 2, -3) == (16, (1, -3), -1)
    assert quadratic2(2, 4, 8) == (-48, (), -1)

def test_quadratic3():
    assert quadratic3(1, 4, 4) == (0, (-2.0), -2.0)
    assert quadratic3(1, 2, -3) == (4, (1, -3), -1)
    assert quadratic3(2, 4, 8) == (-3, (), -1)

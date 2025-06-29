from gcd import  *


def gcd_fixtures():
    return [
        (48, 22, 2),
        (48, 18, 6),
        (11, 13, 1),
        (54, 24, 6),
        (42, 56, 14),
        (48, 180, 12)
    ]


def test_gcd_euclidean_mod():
    for a, b, o in gcd_fixtures():
        assert gcd_euclidean_mod(a, b)[0] == o


def test_gcd_euclidean_subtraction():
    for a, b, o in gcd_fixtures():
        assert gcd_euclidean_subtraction(a, b)[0] == o


def test_gcd_binary_recursive():
    for a, b, o in gcd_fixtures():
        assert gcd_binary_recursive(a, b)[0] == o


def test_gcd_binary_iteration():
    for a, b, o in gcd_fixtures():
        assert gcd_binary_iteration(a, b)[0] == o


def test_lcm():
    assert lcm(21, 6) == 42
    assert lcm(48, 180) == 720
    assert lcm(16, 20) == 80

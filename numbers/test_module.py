from module import  *


def fixtures():
    return [
        (3, 7, 5),
        (4, 11, 3),
        (143, 7, 5),
        (91, 11, 4),
        (77, 13, 12)
    ]


def test_modular_multiplicative_inverse():
    for f in fixtures():
        print(f)
        assert modular_multiplicative_inverse(f[0], f[1]) == f[2]


def test_modular_multiplicative_inverse2():
    for f in fixtures():
        assert modular_multiplicative_inverse2(f[0], f[1]) == f[2]


def test_chinese_remainder_theorem():
    assert chinese_remainder_theorem((5, 3, 10), (7, 11, 13)) == 894

from search import *

def fixtures():
    return [
        ("AABCACAADAABAAABAA", "ABC", 1),
        ("abacaabadcabacabaabb", "abacab", 10),
        ('Lorem ipsum dolor sit amet', 'dolor', 12),
        ('ABC ABCDAB ABCDABCDABDE', "'ABCDABD'", -1)
    ]


def test_search_naive():
    for f in fixtures():
        assert naive(f[0], f[1])[0] == f[2]
        assert naive(f[0], f[1] + "zzzzzcbnfgdghdfgh")[0] == -1


def test_boyer_moore():
    for f in fixtures():
        assert boyer_moore(f[0], f[1])[0] == f[2]
        assert boyer_moore(f[0], f[1] + "zzzzzcbnfgdghdfgh")[0] == -1

def test_prefix_fumction():
    assert prefix_function("abcdabcabcdabcdab")[0] == [0,0,0,0,1,2,3,1,2,3,4,5,6,7,4,5,6]


def test_z_fumction():
    assert z_function("abacabadaba")[0] == [0, 0, 1, 0, 3, 0, 1, 0, 3, 0, 1]



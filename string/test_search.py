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

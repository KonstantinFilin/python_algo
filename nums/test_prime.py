from prime import is_prime, get_primes_less_than, get_multipliers


def is_prime_fixtures():
    return [
        (-1, False),
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (8, False),
        (9, False),
        (10, False),
        (11, True),
        (12, False),
        (13, True),
        (14, False),
        (15, False),
        (16, False),
        (17, True),
        (18, False),
        (19, True),
        (20, False),
    ]


def test_is_prime():
    for i, o in is_prime_fixtures():
        assert o == is_prime(i)


def test_primes_less_than():
    assert get_primes_less_than(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert get_primes_less_than(20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_get_multipliers():
    assert get_multipliers(1) == {}
    assert get_multipliers(2) == {}
    assert get_multipliers(3) == {}
    assert get_multipliers(4) == {2: 2}

    assert get_multipliers(100) == {2: 2, 5: 2}
    assert get_multipliers(125) == {5: 3}
    assert get_multipliers(609) == {3: 1, 7: 1, 29: 1}

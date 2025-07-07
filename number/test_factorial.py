from factorial import factorial1,factorial_recursive


def factorial_fixtures():
    return [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
        (7, 5040),
        (8, 40320)
    ]


def test_factorial1():
    for i,o in factorial_fixtures():
        ans = factorial1(i)
        assert ans[0] == o


def test_factorial_recursive():
    for i,o in factorial_fixtures():
        ans = factorial_recursive(i)
        assert ans == o

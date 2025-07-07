from arithmetic import arithmetic


def test_arithmetic():
    ans1 = arithmetic(1, 1, 15)
    assert ans1[0] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert ans1[1] == 120

    ans2 = arithmetic(3, 3, 20)
    assert ans2[0] == [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]
    assert ans2[1] == 630

    ans3 = arithmetic(99, -7, 15)
    assert ans3[0] == [99, 92, 85, 78, 71, 64, 57, 50, 43, 36, 29, 22, 15, 8, 1]
    assert ans3[1] == 750

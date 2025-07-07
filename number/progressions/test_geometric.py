from geometric import geometric


def test_geometric():
    ans1 = geometric(2, 2, 10)
    assert ans1[0] == [2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0, 256.0, 512.0, 1024.0]
    assert ans1[1] == 2046

    ans2 = geometric(3, 3)
    assert ans2[0] == [3.0, 9.0, 27.0, 81.0, 243.0, 729.0, 2187.0, 6561.0, 19683.0, 59049.0]
    assert ans2[1] == 88572.0

    ans3 = geometric(4, 5)
    assert ans3[0] == [4.0, 20.0, 100.0, 500.0, 2500.0, 12500.0, 62500.0, 312500.0, 1562500.0, 7812500.0]
    assert ans3[1] == 9765624.0


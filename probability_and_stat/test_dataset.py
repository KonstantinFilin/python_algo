from dataset import Dataset


def fixtures_empty():
    return Dataset([])


def fixtures_dec():
    return Dataset([i for i in range(1, 11)])


def fixtures_1_to_7():
    return Dataset([i for i in range(1, 8)])


def fixtures_ex1():
    items = [0, 1, 1, 2, 3, 4, 4, 5, 5, 5]
    return Dataset(items)


def fixtures_ex2():
    items = [8050, 8480, 8590, 8340, 8190, 7790, 8290, 7890, 7970, 7910]
    return Dataset(items)


def test_get_len():
    assert fixtures_empty().get_len() == 0
    assert fixtures_dec().get_len() == 10
    assert fixtures_ex1().get_len() == 10
    assert fixtures_ex2().get_len() == 10


def test_get_min():
    assert fixtures_empty().get_min() is None
    assert fixtures_dec().get_min() == 1
    assert fixtures_ex1().get_min() == 0
    assert fixtures_ex2().get_min() == 7790


def test_get_max():
    assert fixtures_empty().get_max() is None
    assert fixtures_dec().get_max() == 10
    assert fixtures_ex1().get_max() == 5
    assert fixtures_ex2().get_max() == 8590


def test_get_range():
    assert fixtures_empty().get_range() is None
    assert fixtures_dec().get_range() == 9
    assert fixtures_1_to_7().get_range() == 6
    assert fixtures_ex1().get_range() == 5
    assert fixtures_ex2().get_range() == 800


def test_get_mid_range():
    assert fixtures_empty().get_mid_range() is None
    assert fixtures_dec().get_mid_range() == 5.5
    assert fixtures_1_to_7().get_mid_range() == 4
    assert fixtures_ex1().get_mid_range() == 2.5
    assert fixtures_ex2().get_mid_range() == 8190


def test_get_average_arithmetic():
    assert fixtures_empty().get_average_arithmetic() is None
    assert fixtures_dec().get_average_arithmetic() == 5.5
    assert fixtures_1_to_7().get_average_arithmetic() == 4
    assert fixtures_ex1().get_average_arithmetic() == 3
    assert fixtures_ex2().get_average_arithmetic() == 8150


def test_get_median():
    assert fixtures_empty().get_median() is None
    assert fixtures_dec().get_median() == 5.5
    assert fixtures_1_to_7().get_median() == 4
    assert fixtures_ex1().get_median() == 3.5
    assert fixtures_ex2().get_median() == 8120


def test_get_mode():
    assert fixtures_empty().get_mode() is None
    assert fixtures_dec().get_mode() is None
    assert fixtures_1_to_7().get_mode() is None
    assert fixtures_ex1().get_mode() == 5
    assert fixtures_ex2().get_mode() is None


def test_get_expected_value():
    assert fixtures_empty().get_expected_value() is None
    assert fixtures_dec().get_expected_value() == 5.5
    assert fixtures_1_to_7().get_expected_value() == 4
    assert fixtures_ex1().get_expected_value() == 3
    assert fixtures_ex2().get_expected_value() == 8150

    ds = Dataset([0, 200, 2000])
    ds.set_probability_table({0: 0.89, 200: 0.1, 2000: 0.01})
    assert ds.get_expected_value() == 40

def test_get_variance():
    ds1 = Dataset([1, 2, 5])
    ds1.set_probability_table({1:0.3, 2: 0.5, 5:0.2})
    assert ds1.get_variance() == 2.01

    assert fixtures_empty().get_variance() is None
    assert fixtures_dec().get_variance() == 8.25
    assert fixtures_1_to_7().get_variance(1) == 4
    assert fixtures_ex1().get_variance(0) == 3
    assert fixtures_ex2().get_variance() == 65700

    ds2 = Dataset([1, 2, 3])
    ds2.set_probability_table({1:0.4, 2: 0.1, 3:0.3})
    assert ds2.get_variance() == 1.25

    ds3 = Dataset([-3, -2, -1, 0])
    ds3.set_probability_table({-3: 0.2, -2: 0.3, -1: 0.3, 0: 0.3})
    assert ds3.get_variance() == 1.05


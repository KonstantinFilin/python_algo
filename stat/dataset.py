import math
from decimal import *


class Dataset:
    def __init__(self, items) -> None:
        self.items = items
        self.probability_table = []
        # getcontext().prec = 10

    def get_len(self) -> int:
        return len(self.items) if self.items else 0

    def get(self) -> list:
        return self.items

    def get_min(self) -> float:
        return min(self.items) if self.items else None

    def get_max(self) -> float:
        return max(self.items) if self.items else None

    def get_average_arithmetic(self) -> float:
        return sum(self.items)/self.get_len() if self.items else None

    def get_range(self) -> float:
        return self.get_max() - self.get_min() if self.items else None

    def get_mid_range(self) -> float:
        return (self.get_max() + self.get_min()) / 2 if self.items else None

    def get_standart_variation(self, precision = 10):
        return math.sqrt(self.get_variance())

    def get_variance(self, precision = 10):
        if not self.items:
            return None

        res = 0
        pt = self.get_probability_table()
        ex = self.get_expected_value()
        ex2 = ex**2

        for x,p in pt.items():
            res = round(x*x*p + res, precision)

        return float(round(Decimal(res) - ex2, precision))

    def get_expected_value(self):
        if not self.items:
            return None

        res = Decimal(0)
        pt = self.get_probability_table()

        for x,p in pt.items():
            d = Decimal(round(x*Decimal(p), 2))
            res = round(round(d, 2) + res, 2)

        return res

    def get_mode(self):
        if not self.items:
            return None

        ft = self.get_frequency_table()
        max_f = None
        max_v = None
        diff_freq = False

        for v, f in ft.items():
            if max_v and max_f != f:
                diff_freq = True

            if not max_f or max_f < f:
                max_f = f
                max_v = v

        return max_v if diff_freq else None

    def get_median(self):
        if not self.items:
            return None

        arr = sorted(self.items)

        if self.get_len() % 2 != 0:
            return arr[(self.get_len() - 1) // 2]

        idx = self.get_len() // 2

        return (arr[idx - 1] + arr[idx]) / 2

    def get_frequency_table(self):
        stat = {}

        for i in self.items:
            if i not in stat:
                stat[i] = 0

            stat[i] += 1

        return stat

    def set_probability_table(self, pt):
        self.probability_table = pt

    def get_probability_table(self):
        if self.probability_table:
            return self.probability_table

        l = len(self.items)

        stat = {}

        for i in self.items:
            if i not in stat:
                stat[i] = 0

            stat[i] += round(1/l, 3)

        return stat
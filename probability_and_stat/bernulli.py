from nums.binom import *


def n_failures_exactly_and_one_success(p:float, n: int)->float:
    return p * (1 - p)**n

def n_failures_max(p: int, n: int)->float:
    return 1 - (1 - p)**n

def f_failures_and_s_successes_exactly(p:float, s: int, f: float):
    return p**s * (1 - p)**f

def m_successes_in_n_tests(m: int, n: int, p: float)->float:
    return get_binom_coefficient(m, n) * f_failures_and_s_successes_exactly(p, m, n)


if __name__ == "__main__":
    print(m_successes_in_n_tests(0, 6, 0.3))

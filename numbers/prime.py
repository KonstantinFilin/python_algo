import math


def get_multipliers(n):
    if is_prime(n):
        return {}

    ret = {}
    primes = get_primes_less_than(n - 1)
    n_pre = 0

    while 1 < n != n_pre:
        for p in primes:
            if n % p == 0:
                n_pre = n
                n = n / p

                if p in ret:
                    ret[p] += 1
                else:
                    ret[p] = 1

                break

    return ret


def get_primes_less_than(n):
    ret = []

    for i in range (2, n + 1):
        if is_prime(i):
            ret.append(i)

    return ret


def is_prime(n):
    if n <= 1:
        return False

    e = int(math.sqrt(n)) + 1

    for i in range(2, e):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    import sys
    # ans = is_prime(int(sys.argv[1]))
    is_prime(25);
    ans = 15
    print("Is prime" if ans else "Is NOT prime")

    print(get_primes_less_than(int(sys.argv[1])))
    print(get_multipliers(int(sys.argv[1])))


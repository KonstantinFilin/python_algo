"""
GCD - Greatest common divisor
LCM - Least common multiple
"""


def gcd_euclidean_extended(a, b, log=[]):
    s = 0
    r = b
    x = 1
    d = a
    log = ['a', 'b', 'd', 'x', 'y']

    while r != 0:
        log.append((a, b, d, x, 0))
        quotient = d // r
        d, r = r, d - quotient * r
        x, s = s, x - quotient * s

    if b != 0:
        y = (d - x * a) // b
    else:
        y = 0

    log.append((a, b, d, x, y))
    ret = d, x, y

    return ret, log


def gcd_euclidean_mod(a, b):
    log = [('a', 'b')]

    while b != 0:
        log.append((a, b))
        a, b = b, a % b

    return a, log


def gcd_euclidean_subtraction(a, b):
    log = [('a', 'b')]

    while b != 0:
        log.append((a, b))
        if a > b:
            a -= b
        else:
            b -= a

    return a, log


def lcm(a, b):
    return abs(a*b) / gcd_euclidean_mod(a, b)[0]


def gcd_binary_recursive(a, b, log=[]):

    if len(log) == 0:
        log = [('a', 'b')]

    log.append((a, b))

    if a == 0:
        return b, log

    if b == 0:
        return a, log

    if a == b:
        return a, log

    if a == 1 or b == 1:
        return 1, log

    if a % 2 == 0 and b % 2 == 0:
        ans, log = gcd_binary_recursive(a / 2, b / 2, log)
        return 2 * ans, log

    if a % 2 == 0 and b % 2 != 0:
        return gcd_binary_recursive(a / 2, b, log)

    if a % 2 != 0 and b % 2 == 0:
        return gcd_binary_recursive(a, b / 2, log)

    if a % 2 != 0 and b % 2 != 0:
        if a > b:
            return gcd_binary_recursive(b, (a - b) / 2, log)
        else:
            return gcd_binary_recursive((b - a) / 2, a, log)


def gcd_binary_iteration(a, b):
    log = [('a', 'b', 'multiplier')]
    multiplier = 1

    while a != 0 and b != 0 and a != b and a != 1 and b != 1:
        log.append((a, b, multiplier))

        if a % 2 == 0 and b % 2 == 0:
            multiplier *= 2
            a, b = a / 2, b / 2

        if a % 2 == 0 and b % 2 != 0:
            a = a / 2

        if a % 2 != 0 and b % 2 == 0:
            b = b / 2

        if a % 2 != 0 and b % 2 != 0:
            if a > b:
                a, b = b, (a - b) / 2
            else:
                a, b = (b - a) / 2, a

    log.append((a, b))

    if a == 0:
        return b * multiplier, log

    if b == 0:
        return a * multiplier, log

    if a == b:
        return a * multiplier, log

    if a == 1 or b == 1:
        return 1 * multiplier, log

    return 0, ()


if __name__ == "__main__":
    import sys
    ans = gcd_euclidean_mod(int(sys.argv[1]), int(sys.argv[2]))
    print("Euclidean module")
    print(ans[0])
    print(ans[1])
    print()

    ans = gcd_euclidean_subtraction(int(sys.argv[1]), int(sys.argv[2]))
    print("Euclidean subtraction")
    print(ans[0])
    print(ans[1])
    print()

    ans = gcd_euclidean_extended(int(sys.argv[1]), int(sys.argv[2]))
    print("Euclidean extended (d, x, y: d = ax + by): ")
    print(ans[0])
    print(ans[1])
    print()

    ans = gcd_binary_recursive(int(sys.argv[1]), int(sys.argv[2]))
    print("Binary recursive")
    print(ans[0])
    print(ans[1])
    print()

    ans = gcd_binary_iteration(int(sys.argv[1]), int(sys.argv[2]))
    print("Binary iteration")
    print(ans[0])
    print(ans[1])

    ans = lcm(int(sys.argv[1]), int(sys.argv[2]))
    print("LCM")
    print(ans)

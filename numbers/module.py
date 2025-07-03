def modular_multiplicative_inverse(num: int, mod: int) -> int:
    for i in range(mod):
        if num * i % mod == 1:
            return i

    return -1


def modular_multiplicative_inverse2(num: int, mod: int) -> int:
    from gcd import gcd_euclidean_extended

    d, x, y = gcd_euclidean_extended(num, mod)[0]

    if x < 0:
        while x < 0:
            x += mod

    if x >= mod:
        while x >= mod:
            x -= mod

    return x


if __name__ == "__main__":

    import sys

    if len(sys.argv) < 3:
        print(f"Usage: python3 {sys.argv[0]} number module")

    num = int(sys.argv[1])
    mod = int(sys.argv[2])

    print("1: " + str(modular_multiplicative_inverse(num, mod)))
    print("2: " + str(modular_multiplicative_inverse2(num, mod)))

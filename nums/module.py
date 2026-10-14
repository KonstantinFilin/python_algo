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


def chinese_remainder_theorem(rest_list, mod_list):
    m = 1
    m_list = []
    y_list = []
    sum = 0;

    for mm in mod_list:
        m *= mm

    for mm in mod_list:
        mi = m / mm
        yi = modular_multiplicative_inverse(mi, mm)
        m_list.append(mi)
        y_list.append(yi)

    for i in range(len(rest_list)):
        sum += rest_list[i] * m_list[i] * y_list[i]

    return sum % m


if __name__ == "__main__":

    import sys

    if len(sys.argv) < 3:
        print(f"Usage: python3 {sys.argv[0]} number module")

    num = int(sys.argv[1])
    mod = int(sys.argv[2])

    print("1: " + str(modular_multiplicative_inverse(num, mod)))
    print("2: " + str(modular_multiplicative_inverse2(num, mod)))

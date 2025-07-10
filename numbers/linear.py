def linear(a, b):
    return b / a


def linear_zeros(a, b):
    return b / a, -b


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("A * X = B")
        print("Usage: python " + sys.argv[0] + " A B")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[2])

    print(f'{a} * x = {b}')
    x = linear(a, b)
    print(f'x = {x}')
    print(f'{a} * {x} = {b}')

    x0, y0 = linear_zeros(a, b)
    print(f'y = 0: x = {x0}; x = 0: y = {y0}')


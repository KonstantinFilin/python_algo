
def geometric(b1, q, n = 10):
    items = [b1]

    for i in range(2, n + 1):
        items.append(b1 * q**(i - 1))

    sum1 = b1 * (1 - q**n) / (1 - q)

    return items, sum1


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: python " + sys.argv[0] + " b1 q n=10")
        exit(1)

    b1 = float(sys.argv[1])
    q = float(sys.argv[2])
    n = 10

    if len(sys.argv) >= 4:
        n = int(sys.argv[3])

    ans = geometric(b1, q, n)

    print("Items: ")
    print(ans[0])
    print("Sum: ")
    print(ans[1])

def arithmetic(a1, d, n = 10):
    items = [a1]

    for i in range(2, n + 1):
        items.append(a1 + (i - 1) * d)

    sum1 = n * (items[0] + items[-1]) / 2

    return items, sum1


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: python " + sys.argv[0] + " a1 d n=10")
        exit(1)

    a1 = int(sys.argv[1])
    d = int(sys.argv[2])
    n = 10

    if len(sys.argv) >= 4:
        n = int(sys.argv[3])

    ans = arithmetic(a1, d, n)

    print("Items: ")
    print(ans[0])
    print("Sum: ")
    print(ans[1])
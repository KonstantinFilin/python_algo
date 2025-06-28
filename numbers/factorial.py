
def factorial1(n):
    log = [('#', 'n', 's')]

    if n ==0 or n == 1:
        return 1, log

    cnt = 0
    s = n

    while n > 1:
        cnt += 1
        log.append((cnt, n, s))
        n -= 1
        s *= n

    log.append((cnt + 1, n, s))

    return s, log


def factorial_recursive(n):
    if n ==0 or n == 1:
        return 1

    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    import sys
    ans = factorial1(int(sys.argv[1]))
    ans2 = factorial_recursive(int(sys.argv[1]))
    print ("factorial1: " + str(ans[0]))
    print ("factorial_recursive: " + str(ans2))
    print ()

    cnt = 0
    for l in ans[1]:
        print("\t".join(map(str, l)))
        if cnt == 0:
            print ("-" * 100)

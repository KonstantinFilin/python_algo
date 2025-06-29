def fibo(n):
    if n < 1:
        return []

    a = 1
    b = 1
    ret = [a]

    if n == 1:
        return ret

    ret.append(b)

    if n == 2:
        return ret

    for _ in range(3, n + 1):
        a, b = b, a + b
        ret.append(b)

    return ret


if __name__ == "__main__":
    import sys
    ans = fibo(int(sys.argv[1]))
    print(ans)

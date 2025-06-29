import math


def quadratic(a, b, c):
    d = b*b - 4 * a * c
    roots = ()

    if d == 0:
        roots = (-b / (2 * a))
    elif d > 0:
        d_root = math.sqrt(d)
        roots = ( (-b + d_root) / (2 * a), (-b - d_root) / (2 * a) )

    return d, roots, -b / (2 * a)


def quadratic2(a, b, c):
    d = b*b - 4 * a * c
    roots = ()

    if d == 0:
        roots = (2*c / -b)
    elif d > 0:
        d_root = math.sqrt(d)
        roots = ( (2 * c) / (-b - d_root), (2 * c) / (-b + d_root) )

    return d, roots, -b / (2 * a)


def quadratic3(a, b, c):
    p = b / a
    q = c / a
    d = (p / 2)**2  - q
    roots = ()

    if d == 0:
        roots = (-p/2)
    elif d > 0:
        d_root = math.sqrt(d)
        roots = (-p/2 + d_root, -p/2 - d_root)

    return d, roots, -b / (2 * a)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 4:
        print("A*X^2 + B*X + C = 0")
        print("Usage: python " + sys.argv[0] + " A B C")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])

    sign_b = "+" if b >= 0 else "-"
    sign_c = "+" if c >= 0 else "-"

    print(f"{a}*X^2 {sign_b} {abs(b)}*X {sign_c} {abs(c)} = 0")

    ans = quadratic(a, b, c)

    print(f"D = {ans[0]}")
    print(f"Roots: {ans[1]}")
    print(f"x min/max:: {ans[2]}")

def get_binom_coefficient(k: int, n: int)->int:
    pt = get_pascal_triangle(n)
    return pt[n][k]

def get_pascal_triangle(n: int)->list[list[int]]:
    ret: list[list[int]] = [] # [[0]*(n + 1)]*(n + 1)

    for _ in range(n + 1):
        ret.append([0]*(n + 1))

    for i in range(n + 1):
        for j in range(n + 1):
            if j == 0:
                ret[i][j] = 1
            elif i == 0:
                ret[i][j] = 0
            else:
                ret[i][j] = ret[i - 1][j - 1] + ret[i - 1][j]

    return ret


if __name__ == "__main__":
    print(get_pascal_triangle(5))
    print(get_binom_coefficient(4, 10)) # 210

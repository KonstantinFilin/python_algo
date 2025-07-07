def naive(haystack, needle):
    len_needle = len(needle)
    len_haystack = len(haystack)

    log = [('c1', 'c2', 'cur_needle', 'len_needle')]

    for cur_haystack in range(0, len_haystack - len_needle + 1):
        cur_needle = 0

        while cur_needle < len_needle:
            c1 = haystack[cur_haystack + cur_needle]
            c2 = needle[cur_needle]

            log.append((c1, c2, cur_needle, len_needle))

            if c1 != c2:
                break

            cur_needle += 1

        if cur_needle == len_needle:
            return cur_haystack, log

    print("Pattern not found")
    return -1, log


if __name__ == '__main__':
    s = "AABCACAADAABAAABAA"
    ss = "ABC"
    ans = naive(s, ss)

    print(ans)

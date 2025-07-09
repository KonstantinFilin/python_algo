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

    return -1, log


def rabin_karp(haystack, needle):
    result = []
    log = []

    haystack = haystack.upper()
    needle = needle.upper()

    l = len(haystack)
    l_p = len(needle)
    con = 26

    hash_value = 0
    current_hash = 0

    for i in range(l_p):
        hash_value += (ord(needle[i]) - ord('A') + 1) * (con ** (l_p - i - 1))
        current_hash += (ord(haystack[i]) - ord('A') + 1) * (con ** (l_p - i - 1))

    for ind in range(l - l_p + 1):
        if ind != 0:
            current_hash = con * (current_hash - ((ord(haystack[ind - 1]) - ord('A') + 1) * (con ** (l_p - 1)))) \
                   + (ord(haystack[ind + l_p - 1]) - ord('A') + 1)

        log.append((ind, current_hash, hash_value))

        if current_hash == hash_value:
            result.append(ind)

    print("End")

    return result, log


def boyer_moore(haystack, needle):
    """Find occurrence of pattern in text."""
    log = [('i', 'j', 'n', 'm', 'haystack[i]', 'needle[j]')]
    alphabet = set(haystack)
    last = last_occurrence(needle, alphabet)
    m = len(needle)
    n = len(haystack)
    i = m - 1  # text index
    j = m - 1  # pattern index
    while i < n:
        log.append((i, j, n, m, haystack[i], needle[j]))

        if haystack[i] == needle[j]:
            if j == 0:
                return i, log
            else:
                i -= 1
                j -= 1
        else:
            l = last(haystack[i])
            i = i + m - min(j, 1 + l)
            j = m - 1

    return -1, log


class last_occurrence(object):
    """Last occurrence functor."""

    def __init__(self, pattern, alphabet):
        """Generate a dictionary with the last occurrence of each alphabet
        letter inside the pattern.

        Note: This function uses str.rfind, which already is a pattern
        matching algorithm. There are more 'basic' ways to generate this
        dictionary."""
        self.occurrences = dict()
        for letter in alphabet:
            self.occurrences[letter] = pattern.rfind(letter)

    def __call__(self, letter):
        """Return last position of the specified letter inside the pattern.
        Return -1 if letter not found in pattern."""
        return self.occurrences[letter]


def prefix_function(s):
    prefix = [0] * len(s)
    log = [('prefix', 'i', 'k', 's[k]', 's[i]')]

    for i in range(1, len(s)):
        k = prefix[i - 1]

        log.append((prefix, i, k, s[k], s[i]))

        while k > 0 and s[k] != s[i]:
            k = prefix[k - 1]

        if s[k] == s[i]:
            k += 1

        prefix[i] = k

    return prefix, log


def z_function(s):
    s += '$'
    l, r = 0, 0
    z = [0] * len(s)
    log = [('i', 's', 'l', 'r', 'z')]

    for i in range(1, len(s)):
        log.append((i, s, l, r, z))
        z[i] = max(0, min(z[i - l], r - i))

        while s[z[i]] == s[i + z[i]]:
            z[i] += 1

        if i + z[i] > r:
            l, r = i, i + z[i]

    return z[:-1], log


def knuth_morris_pratt(haystack, needle):
    index = -1
    f = prefix_function(needle)[0]
    k = 0
    log = []

    for i in range(len(haystack)):

        log.append((i, k, index, f))

        while k > 0 and (needle[k] != haystack[i]):
            k = f[k - 1]

        if needle[k] == haystack[i]:
            k = k + 1

        if k == len(needle):
            index = i - len(needle) + 1
            break

    return index, log


if __name__ == '__main__':
    s = "AABCACAADAABAAABAA"
    ss = "ABC"

    ans = naive(s, ss)
    print("Naive:")
    print(ans[0])
    print(ans[1])

    ans = boyer_moore(s, ss)
    print("boyer_moore:")
    print(ans[0])
    print(ans[1])

    ans = prefix_function(s)
    print("Prefix function:")
    print(ans[0])
    print(ans[1])

    ans = z_function(s)
    print("Z-function:")
    print(ans[0])
    print(ans[1])

    ans = knuth_morris_pratt(s, ss)
    print("Knuth–Morris–Pratt:")
    print(ans[0])
    print(ans[1])

    ans = rabin_karp(s, ss)
    print("Rabin-Karp:")
    print(ans[0])
    print(ans[1])

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


def rabin_karp(haystack, needle, d, q):
    n = len(haystack)
    m = len(needle)
    h = pow(d, m-1) % q
    p = 0
    t = 0
    result = []

    for i in range(m): # preprocessing
        p = (d * p + ord(needle[i])) % q
        t = (d * t + ord(haystack[i])) % q

    for s in range(n - m + 1): # note the +1
        if p == t: # check character by character
            match = True
            for i in range(m):
                if needle[i] != haystack[s + i]:
                    match = False
                    break
            if match:
                result = result + [s]
        if s < n-m:
            t = (t - h * ord(haystack[s])) % q # remove letter s
            t = (t * d + ord(haystack[s + m])) % q # add letter s+m
            t = (t + q) % q # make sure that t >= 0

    return result


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
            k = prefix[k-1]

        if s[k] == s[i]:
            k += 1

        prefix[i] = k

    return prefix, log


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

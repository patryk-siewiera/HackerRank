def gcdIter(a, b):
    higher = a
    lower = b
    if b > a:
        higher = b
        lower = a
    astart = higher
    score = 1

    while score > 0:
        mod = b % astart
        mod2 = a % astart
        score = mod + mod2
        astart -= 1
    return astart + 1

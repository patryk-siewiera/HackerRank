def gcdRecur(a, b):
    higher = a
    lower = b
    if b > a:
        higher = b
        lower = a
    modulus = a % b
    if modulus != 0:
        return gcdRecur(a=b, b=modulus)
    else:
        return b
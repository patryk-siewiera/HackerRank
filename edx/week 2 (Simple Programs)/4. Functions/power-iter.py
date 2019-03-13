# week2
# power-iter
def iterPower(base, exp):
    if exp == 0:
        return 1

    score = base
    while exp > 1:
        exp -= 1
        score *= base
    return score

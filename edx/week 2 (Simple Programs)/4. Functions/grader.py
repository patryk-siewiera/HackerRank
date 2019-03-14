# def polysum -> take 2 arugments -> n s
# import from math -> tan, pi
# return sum, rounded to 4 decimal places

import math


def polysum(n, s):
    high = 0.25 * n * s ** 2
    low = math.tan(math.pi / n)
    score = high / low
    per = (n * s) ** 2
    output = score + per
    output = round(output, 4)
    return output


print(polysum(88, 79))

# 6 kyu

# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
#
# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)
#
# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)


def find_outlier(integers):
    even = 0
    odd = 0
    position_even = 0
    position_odd = 0

    # determine what numbers is more: even or odd
    for i in range(len(integers)):
        if (integers[i] % 2) == 0:
            even += 1
            position_even = i
        else:
            odd += 1
            position_odd = i

    if (even < odd):
        return integers[position_even]
    else:
        return integers[position_odd]


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
# == 3

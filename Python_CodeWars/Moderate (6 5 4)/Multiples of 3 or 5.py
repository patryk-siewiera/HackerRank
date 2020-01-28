# 6 kyu

#  If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
#
# Note: If the number is a multiple of both 3 and 5, only count it once.
#
# Courtesy of ProjectEuler.net


def solution(number):
    output = []
    for i in range(number):
        div = (i / 3)
        if div % 1 == 0:
            output.append(div * 3)

    for j in range(number):
        div = (j / 5)
        if div % 1 == 0:
            output.append(div * 5)

    output = [int(k) for k in set(output)]
    return sum(output)


print(solution(10))
# should be 23

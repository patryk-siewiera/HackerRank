# 7kyu

# Welcome. In this kata, you are asked to square every digit of a number.
#
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
#
# Note: The function accepts an integer and returns an integer

def square_digits(num):
    # convert to list
    num = list(str(num))
    # convert to list of int
    num = [int(i) for i in num]

    square = [j * j for j in num]
    square_str = [str(k) for k in square]
    square_str_join = "".join(square_str)
    int_square = int(square_str_join)

    return int_square


square_digits(9119)

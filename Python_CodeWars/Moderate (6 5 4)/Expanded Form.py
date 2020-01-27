# 6 kyu
#
# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:
#
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.


def expanded_form(num):
    num_str = str(num)
    length = len(num_str)
    output_list = []
    output_string = ""

    for num in range(length):
        number = num_str[num]
        if int(number) == 0:
            continue
        power = 10 ** (length - num - 1)
        output_list.append(power * int(number))
        output_string += str(power * int(number)) + " + "

    return output_string[:-3]


print(expanded_form(1002003))
# should return == '10+2'

import re
from collections import Counter

# TODO: problem -> it count occurence in whole, not in context of previous

# group() - returns one or more subgroups
# groups() - returns tuple
# groupdict() - dictionary all named subgroups of the match


def user_input():
    user_inputs = input()
    return user_inputs


def sample_input():
    str_test = '..12345678910111213141516171820212223'
    return str_test


def parse_numbers(str_to_parse):
    regex = re.compile(r'[a-zA-Z0-9]+')
    numbers_parsed = re.findall(regex, str_to_parse)
    numbers_parsed = "".join(numbers_parsed)
    return numbers_parsed


def check_repetition(numbers):
    strNumbers = str(numbers)
    newList = [0]
    for j in strNumbers:
        newList.append(j)

    # counted = (Counter(newList))
    # print(counted.values())

    for i in range(len(strNumbers) - 1):
        sliced_list = (newList[0:i + 1])
        counted = (Counter(sliced_list))
        sorted_values = (sorted(counted.values()))
        sorted_again = (sorted_values[::-1])

        state = False

        if sorted_again[0] > 1:
            state = True
            return print(sliced_list[i])

    if (state == False):
        print(-1)


numbers = parse_numbers(user_input())
check_repetition(numbers)

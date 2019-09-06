import re


# group() - returns one or more subgroups
# groups() - returns tuple
# groupdict() - dictionary all named subgroups of the match


def user_input():
    user_inputs = input()
    return user_inputs


def sample_input():
    str_test = '1234sncsdncsjnsjkdcn'
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

    for i in range(len(strNumbers) - 2):
        statement = False
        sliced_list = (newList[0:i + 2])
        last_element = sliced_list[-1]
        last_previous = sliced_list[-2]

        if last_element == last_previous:
            statement = True
            return print(last_element)

    if statement == False:
        print(-1)


numbers = parse_numbers(user_input())
check_repetition(numbers)

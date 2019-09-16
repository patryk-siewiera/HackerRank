import re

sample_input = 'rabcdeefgyYhFjkIoom3123,.npOeorteeeeet'


def user_input():
    return input()


def findall(str_find):
    # search for non-overlaping patterns
    output = re.findall(r'ee', str_find)
    return output


def finditer(str_find):
    # return iterator yielding MachObject instances over
    # all non-overlapping matches for the re pattern in the string
    output = re.finditer(r'ee', str_find)
    # output = map(lambda x: x.group(), re.finditer(r'\w', 'http://www.hackerrank.com/'))
    return output


# print(findall(sample_input))
iter_out = (finditer(sample_input))
print(iter_out)

# 5 kyu

# Hey You !
# Sort these integers for me ...
#
# By name ...
#
# Do it now !
#
# Input
# Range is 0-999
#
# There may be duplicates
#
# The array may be empty
#
# Example
# Input: 1, 2, 3, 4
# Equivalent names: "one", "two", "three", "four"
# Sorted by name: "four", "one", "three", "two"
# Output: 4, 1, 3, 2
# Notes
# Don't fret about formatting rules. If rules are consistently applied it has no effect anyway:
# e.g. one hundred one, one hundred two is same order as one hundred and one, one hundred and two
# e.g. ninety eight, ninety nine is same order as ninety-eight, ninety-nine
def sort_by_name(arr):
    output = []
    for i in range(len(arr)):
        output.append([num2words(arr[i]), arr[i]])
    output.sort()

    # print only second item
    numbers_output = []
    for j in range(len(output)):
        numbers_output.append(output[j][1])
    return numbers_output


def num2words(num):
    under_20 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven',
                'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    above_100 = {100: 'Hundred', 1000: 'Thousand', 1000000: 'Million', 1000000000: 'Billion'}

    if num < 20:
        return under_20[num]

    if num < 100:
        return tens[(int)(num / 10) - 2] + ('' if num % 10 == 0 else ' ' + under_20[num % 10])

    # find the appropriate pivot - 'Million' in 3,603,550, or 'Thousand' in 603,550
    pivot = max([key for key in above_100.keys() if key <= num])

    return num2words((int)(num / pivot)) + ' ' + above_100[pivot] + (
        '' if num % pivot == 0 else ' ' + num2words(num % pivot))
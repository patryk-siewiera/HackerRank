# 7 kyu

# Return the number (count) of vowels in the given string.
#
# We will consider a, e, i, o, and u as vowels for this Kata.
#
# The input string will only consist of lower case letters and/or spaces.

def getCount(inputStr):
    num_vowels = 0
    vowels = "aeiou"
    inputStr = inputStr.lower()
    score = 0

    for i in range(len(inputStr)):
        if inputStr[i] in vowels:
            score += 1

    return score


print(getCount("abracadabra"))
# should be 5

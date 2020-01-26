# 6 kyu

# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence
# "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is
# irrelevant). Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore
# numbers and punctuation.

import string


def is_pangram(s):
    # create dictionary alphabet
    new_dict = dict()
    alphabet = string.ascii_lowercase

    for letter in alphabet:
        new_dict[letter] = 0

    # convert string to lowercase list

    s = list(s.lower())

    # count to dictionary only if is there

    for i in s:
        if i in alphabet:
            new_dict[i] += 1

    # print all keys with value 0

    for j, k in new_dict.items():
        if k == 0:
            return False

    return True

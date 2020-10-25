# 5 kyu Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the
# following form :
#
#  "(p1**n1)(p2**n2)...(pk**nk)"
# where a ** b means a to the power of b
#
# with the p(i) in increasing order and n(i) empty if n(i) is 1.
#
# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"


# Notes:

#TODO unfinished


def primeFactors(n):
    pass


def tests():
    print(primeFactors(7775460) == "(2**2)(3**3)(5)(7)(11**2)(17)")


# tests()

#%%
def find_all_primes(max_number):
    list_primes = []
    for tested_number in range(2, max_number):
        for current_number in range(2, max_number):
            if (current_number / tested_number) == 0:
                print((current_number / tested_number))
            else:
                list_primes.append(tested_number)
    return list_primes


"""
returns: list of primes
"""

#
# find_all_primes(20)
# primes = [2, 3, 5, 7, 11, 13, 17, 19]

print(find_all_primes(10))
#%%
primes_10 = [2, 3, 5, 7]


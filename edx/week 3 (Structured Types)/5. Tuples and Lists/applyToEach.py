# applyToEach


def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


testList = [1, -4, 8, -9]

applyToEach(testList, abs)
print("abs: ", testList)


def inc(a):
    return a + 1


testList = [1, -4, 8, -9]
applyToEach(testList, inc)
print("inc: ", testList)


def power(b):
    return b * b


testList = [1, -4, 8, -9]
applyToEach(testList, power)
print("power: ", testList)

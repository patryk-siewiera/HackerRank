import numpy

myTup = tuple(map(int, input().split()))

print(numpy.zeros(myTup, dtype=int))
print(numpy.ones(myTup, dtype=int))

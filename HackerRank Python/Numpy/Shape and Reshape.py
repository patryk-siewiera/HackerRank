import numpy

arr = [int(x) for x in input().split()]
new_array = numpy.reshape(arr,(3,3))
print(new_array)
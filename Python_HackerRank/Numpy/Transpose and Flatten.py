import numpy

# transpose - change x with y
# flatten - everything in one dimension

x, y = list(map(int, input().split()))

arr = numpy.array([input().strip().split() for _ in range(x)], int)

print(numpy.transpose(arr).astype(int))
print(arr.flatten().astype(int))

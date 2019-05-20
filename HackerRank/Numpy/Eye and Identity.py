import numpy

a, b = map(int, input().split())
numpy.set_printoptions(sign=' ')
print(numpy.eye(a, b))

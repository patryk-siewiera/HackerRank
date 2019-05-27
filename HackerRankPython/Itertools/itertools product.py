from itertools import product

a = set(map(int, input().split()))
b = set(map(int, input().split()))

c = tuple(product(a, b))
print(*c) #upacking tuple!
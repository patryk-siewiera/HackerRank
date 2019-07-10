x = input()
a = set(map(int, input().split()))
x = input()
b = set(map(int, input().split()))

c = a.union(b)
d = a.intersection(b)
e = c.difference(d)
f = list(e)
f.sort()
for i in range(len(f)):
    print(f[i])

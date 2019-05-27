import collections

a = int(input())
b = list(map(int, input().split()))
c = (collections.Counter(b))
for key, value in c.items():
    if value == 1:
        print(key)
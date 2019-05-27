from collections import Counter

numberOfShoes = int(input())
shoeSizes = Counter(map(int, input().split()))
nCustomers = int(input())

summary = 0

for _ in range(nCustomers):
    size, price = (map(int, input().split()))
    if shoeSizes[size]:
        summary += price
        shoeSizes[size] -= 1

print(summary)

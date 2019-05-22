x, y = map(int, input().split())
myList = []

for i in range(y):
    myList.append(map(float, input().split()))

for k in zip(*myList):
    print(sum(k) / len(k))

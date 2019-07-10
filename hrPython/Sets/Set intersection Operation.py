a = input()
mySet = set(map(int, input().split()))
b = input()
mySet2 = set(map(int, input().split()))

c = mySet.intersection(mySet2)
print(len(c))

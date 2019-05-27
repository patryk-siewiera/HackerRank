a = input()
mySet = set(map(int, input().split()))
b = input()
mySet2 = set(map(int, input().split()))

c = mySet.union(mySet2)
print(len(c))

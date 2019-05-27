a = input()
mySet = set(map(int, input().split()))
b = input()
mySet2 = set(map(int, input().split()))

c = mySet.symmetric_difference(mySet2)
print(len(c))

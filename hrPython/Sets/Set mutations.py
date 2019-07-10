# update = adding
# intersection_update = keep only elements found in other set
# difference_update = remove elements found in other set
# symetric_difference_update = keep elements not found in both

# n = 16
# mySet = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 24, 52}
# nCommands = 4
# listCommands = []

n = int(input())
mySet = set(map(int, input().split()))
nCommands = int(input())
listCommands = []

for i in range(nCommands * 2):
    listCommands.append(list(input().split()))

for i in range(len(listCommands) // 2):
    currentEVEN = listCommands[i * 2][0]
    currentODD = map(int, (listCommands[i * 2 + 1][:]))
    if currentEVEN == "intersection_update":
        mySet.intersection_update(currentODD)
    elif currentEVEN == "update":
        mySet.update(currentODD)
    elif currentEVEN == "symmetric_difference_update":
        mySet.symmetric_difference_update(currentODD)
    elif currentEVEN == "difference_update":
        mySet.difference_update(currentODD)

print(sum(mySet))

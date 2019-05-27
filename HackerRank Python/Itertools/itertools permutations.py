from itertools import permutations

# inp = ['HACK', 2]

inp = list(input().split())

myList = list(permutations((inp[0]), int(inp[1])))

myList.sort()

for i in range(len(myList)):
    print(''.join(myList[i]))

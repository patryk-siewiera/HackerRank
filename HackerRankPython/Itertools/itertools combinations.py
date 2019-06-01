from itertools import combinations

inp = list(input().split())

for i in range(int(inp[1])):
    myList = list(combinations((sorted(inp[0])), i + 1))
    myList.sort()
    for j in range(len(myList)):
        print("".join(myList[j]))

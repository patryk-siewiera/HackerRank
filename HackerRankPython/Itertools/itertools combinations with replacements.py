from itertools import combinations_with_replacement

inp = list(input().split())

myList = list(combinations_with_replacement((sorted(inp[0])), int(inp[1])))
myList.sort()
for j in range(len(myList)):
    print("".join(myList[j]))

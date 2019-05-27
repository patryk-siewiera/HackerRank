nCases = int(input())

for i in range(nCases):
    nElemA = int(input())
    setA = set(map(int, input().split()))
    nElemB = int(input())
    setB = set(map(int, input().split()))
    print(setA.issubset(setB))

setA = set(map(int, input().split()))
n = int(input())
output = True

for i in range(n):
    sets = set(map(int, input().split()))
    for j in sets:
        if j not in setA:
            output = False

print(output)
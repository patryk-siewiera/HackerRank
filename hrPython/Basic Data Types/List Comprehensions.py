# if __name__ == '__main__':
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

x = 1
y = 2
z = 3
n = 3

nz = z
ny = y
nx = x

output = []
score = []

for z in range(nx + 1):
    for y in range(ny + 1):
        for x in range(nz + 1):
            output = [z, y, x]
            if sum(output) != n:
                score.append(output)

print(score)

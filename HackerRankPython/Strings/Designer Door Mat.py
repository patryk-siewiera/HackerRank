# n = 11
# m = 21

n, m = list(map(int, input().split()))

s_count = n // 2
pattern = []
iterations = n // 2
welcome = "WELCOME"

s = ".|."

for i in range(s_count):
    temp = s * (i * 2 + 1)
    pattern.append(temp)

for i in range(iterations):
    print(pattern[i].center(m, "-"))

print(welcome.center(m, "-"))

for i in range(iterations):
    print(pattern[iterations - i - 1].center(m, "-"))

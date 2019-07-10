import re

n = input()
n = re.split(r"\.|,", n)

for i in range(len(n)):
    print(n[i])

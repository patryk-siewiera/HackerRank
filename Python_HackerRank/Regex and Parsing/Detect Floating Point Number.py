import re

myList = []

for i in range(int(input())):
    myList.append(input())
    print(bool(re.match(r"^[-+]?[0-9]*\.[0-9]+$", str(myList[i]))))

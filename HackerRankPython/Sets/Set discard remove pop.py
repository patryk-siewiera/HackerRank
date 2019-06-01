n = int(input())
mySet = set(map(int, input().split()))
nCommands = int(input())

for i in range(int(nCommands)):
    command = list(input().split())
    if command[0] == "pop":
        mySet.pop()
    elif command[0] == "remove":
        mySet.remove(int(command[1]))
    elif command[0] == "discard":
        mySet.discard(int(command[1]))

print(sum(mySet))

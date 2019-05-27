from collections import deque

commands = []
d = deque()

for i in range(int(input())):
    commands.append(input().split())
    # print(commands[i])
    if commands[i][0] == 'pop':
        d.pop()
    elif commands[i][0] == 'append':
        d.append(commands[i][1])
    elif commands[i][0] == 'appendleft':
        d.appendleft(int(commands[i][1]))
    elif commands[i][0] == 'popleft':
        d.popleft()

print(*d)

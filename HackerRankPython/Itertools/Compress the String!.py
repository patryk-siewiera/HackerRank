from itertools import groupby

N = input()
for k, g in groupby(N):
    print((len(list(g)), int(k)), end=" ")

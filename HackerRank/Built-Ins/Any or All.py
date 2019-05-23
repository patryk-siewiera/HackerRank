def ex():
    print(any([1 > 0, 1 == 0, 1 < 0]))
    print(all([1 > 0, 1 == 0, 1 < 0]))


# ex()

myList = []
n = int(input())
myList = list(map(int, input().split()))
score = True

for i in range(len(myList)):
    if myList[i] < 0:
        score = False

    word = str(myList[i])
    word_rev = str(myList[i])[::-1]

    if word_rev == word:
        print("test")

# print(score)

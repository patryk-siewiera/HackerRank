def ex():
    testList = [1, 2, 3, 4, 5]
    print(any(i * 2 for i in testList))
    print(all(i > 0 for i in testList))


def solution1():
    myList = []
    n = int(input())
    myList = list(map(int, input().split()))
    score = True
    anyScore = False

    # TODO 1) all integers must be positive
    # TODO 2) any integers should be palindrome

    for i in range(len(myList)):
        if myList[i] > 0:  # condition 1: checking if all integers are positive

            word = str(myList[i])  # assigning value
            word_rev = str(myList[i])[::-1]

            if word_rev == word:  # if any of numbers from myList are palidrome
                anyScore = True

        elif myList[i] < 0:
            score = False
            break

    if score == True and anyScore == True:
        print(True)
    else:
        print(False)


def solutionShort():
    numbersList = []
    reverseList = []

    n = int(input())
    numbersList = list(map(int, input().split()))

    isPositive = all(
        int(numbersList[l]) > 0 for l in range(len(numbersList))
    )  # if numbers are positive

    if isPositive == True:
        [
            reverseList.append(int((str(numbersList[w]))[::-1]))
            for w in range(len(numbersList))
        ]  # put in reveseList
        print(
            any(numbersList[i] == reverseList[i] for i in range(len(numbersList)))
        )  # check if any is palindrome
    else:
        print(False)


solutionShort()

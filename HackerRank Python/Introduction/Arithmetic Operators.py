if __name__ == "__main__":
    a = int(input())
    b = int(input())

    if 1 < a and a < 10 ** 10 and 1 < b and b < 10 ** 10:
        firstLine = a + b
        secondLine = a - b
        thirdLine = a * b
        print(firstLine)
        print(secondLine)
        print(thirdLine)
    else:
        raise Exception("Constraints")

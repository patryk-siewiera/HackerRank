if __name__ == "__main__":
    n = int(input())
    # n=10
    cyfra = 0
    tab = []
    for i in range(n):
        tab.append(i + 1)
    str1 = "".join(str(n) for n in tab)
    print(str1)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    i = 0
    list_sort = arr
    list_sort.sort()

    while list_sort[0 - (i + 1)] == list_sort[-1]:
        i += 1
    else:
        print(list_sort[0 - (i + 1)])

if __name__ == "__main__":
    n = int(input())
    if 0 < n <= 20:
        for i in range(n):
            print(i ** 2)
    else:
        raise Exception("error")

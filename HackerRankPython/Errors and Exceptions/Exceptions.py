def ex():
    try:
        print(1 / 0)
    except ZeroDivisionError as e:
        print('error code ', e)


for i in range(int(input())):

    try:
        n, m = list(map(int, input().split()))
        try:
            print(n // m)
        except ZeroDivisionError as e:
            print('Error Code:', e)
    except ValueError as v:
        print('Error Code:', v)

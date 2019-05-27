cube = lambda x: x ** 3


def fibonacci(n):
    n = int(n)
    output = []

    if n == 0:
        output = []
        return output
    if n == 1:
        output = [0]
        return output

    a, c = [0, 0]
    b = 1
    for i in range(n - 1):
        output.append(c)
        c = a + b
        a = b
        b = c

    output.insert(1, 1)
    return output


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

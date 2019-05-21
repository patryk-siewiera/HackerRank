# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())

lista, lista2, names = ([] for i in range(3))
numbers = set()  # initialize set to have collection without multiple occurrences

for _ in range(int(input())):
    name = input()
    score = float(input())
    lista.append([name, score])


def second(val):
    return val[1]


lista.sort(key=second)

for i in range(len(lista)):
    numbers.add(lista[i][1])

numbers = list(numbers)
numbers.sort()

for i in range(len(lista)):
    if numbers[1] == lista[i][1]:
        names.append(lista[i][0])

# print(numbers)

names.sort()

for i in names:
    print(i)

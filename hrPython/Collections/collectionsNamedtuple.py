from collections import namedtuple


def ex1():
    point = namedtuple("point", "x, y")
    pt1 = point(1, 2)
    pt2 = point(3, 4)
    print(pt1, pt2)
    dot_product = (pt1.x * pt2.x) + (pt1.y * pt2.y)
    print(dot_product)


def ex2():
    Car = namedtuple("Car", "Price Mileage Colour Class")
    xyz = Car(Price=10000, Mileage=30, Colour="cyan", Class="Y")
    print(xyz)
    print(xyz.Class)


# n = 5
n = int(input())

l_Id, l_Marks, l_Name, l_Class = ([] for i in range(4))
l_1, l_2, l_3, l_4 = ([] for j in range(4))

for i in range(n + 1):
    id1, id2, id3, id4 = input().split()
    l_1.append(id1)
    l_2.append(id2)
    l_3.append(id3)
    l_4.append(id4)

lista2 = []
lista2 = [l_1] + [l_2] + [l_3] + [l_4]

for i in range(len(lista2)):
    if "MARKS" == lista2[i][0]:
        l_Marks = lista2[i][1:]
        l_Marks = list(map(int, l_Marks))

length = len(l_Marks)
sums = sum(l_Marks)
score = sums / length
score_formatted = "{:2.2f}".format(score)
print(score_formatted)

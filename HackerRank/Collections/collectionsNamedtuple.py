from collections import namedtuple


def ex1():
    point = namedtuple('point', 'x, y')
    pt1 = point(1, 2)
    pt2 = point(3, 4)
    print(pt1, pt2)
    dot_product = (pt1.x * pt2.x) + (pt1.y * pt2.y)
    print(dot_product)


def ex2():
    Car = namedtuple('Car', 'Price Mileage Colour Class')
    xyz = Car(Price=10000, Mileage=30, Colour='cyan', Class='Y')
    print(xyz)
    print(xyz.Class)


ex1()
ex2()

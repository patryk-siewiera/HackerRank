class Other(object):
    def __init__(self, x):
        self.x = x


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # when using print how it's gonna look
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"

    # passing to function two classes
    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    # define how subtraction works between two classes
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)


c = Coordinate(3, 4)
origin = Coordinate(0, 0)
other_point = Coordinate(4, 2)

# print(Coordinate(origin))
print(c)

# check if is instance of this class
print(isinstance(c, Coordinate))
print(isinstance(c, Other))
print(other_point - origin)

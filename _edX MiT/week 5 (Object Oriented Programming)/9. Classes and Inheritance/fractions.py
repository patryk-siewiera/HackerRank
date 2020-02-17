class fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __str__(self):
        return str(self.numer) + " / " + str(self.denom)

    def getNumer(self):
        return self.numer

    def getDemon(self):
        return self.denom


oneHalf = fraction(1, 2)
twoThirds = fraction(2, 3)

print(oneHalf)

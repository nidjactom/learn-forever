class Vector(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Vector'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __repr__(self):
        return 'Vector(' + str(self.x) + ',' + str(self.y) + ')'

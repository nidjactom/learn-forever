class Grader():

    def __str__(self):
        return 'Grader'
    
    def __init__(self, score=0):
        self.score=score

maths = Grader(90)
print('The math score was',maths.score)

maths.score = 101
print('The math score was changed to',maths.score)

class Grades():

    def __str__(self):
        return 'Grades'
    
    def __init__(self,score=0):
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if value > 100 or value <0:
            raise ValueError('Invalid Score')
        self._score = value

math = Grades(90)
print('The math score was',math.score)
try:
    math.score=101
except ValueError:
    print('The score is not allowed')

class ReadOnly():
    @property
    def constant(self):
        return 24

only_read = ReadOnly()
print('The constant has the value:',only_read.constant)
try:
    only_read.constant = 25
except AttributeError:
    print('Properties cannot be changed without a setter')

class HardWay():

    def __str__(self):
        return 'HardWay'

    def __init__(self, value=True):
        self.hardset(value)

    harddoc = 'Properties can have a getter, setter, deleter and doc string'
    def hardset(self,value):
        if value:
            self.way = True
        else:
            self.way = False

    def hardget(self):
        return self.way

    def harddel(self):
        self.way = None

    hard = property(fget=hardget, fset=hardset, fdel=harddel, doc=harddoc)

not_decorated = HardWay()
not_decorated.hard = 'test'
print('The value of not_decorated.hard is', not_decorated.hard)
del not_decorated.hard
print('The value of not_decorated.hard is', not_decorated.hard)
print(HardWay.hard.__doc__)

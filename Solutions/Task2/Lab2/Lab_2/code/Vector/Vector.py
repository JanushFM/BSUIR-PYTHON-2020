from math import sqrt


class Vector:
    def __init__(self, args):
        self.aList = []
        for i in args:
            self.aList.append(i)

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("unsupported operand type(s) for+:{0} and {1}".format(type(self), type(other)))
        elif len(self.aList) != len(other.aList):
            raise Exception("Vectors have different size.")
        return Vector([x1 + x2 for x1, x2 in zip(self.aList, other.aList)])

    def __sub__(self, other):
        if type(self) is not type(other):
            raise TypeError("unsupported operand type(s) for+:{0} and {1}".format(type(self), type(other)))
        elif len(self.aList) != len(other.aList):
            raise Exception("Vectors have different size.")
        return Vector([x1 - x2 for x1, x2 in zip(self.aList, other.aList)])

    def __mul__(self, other):
        if type(other) is not Vector:
            if type(other) is int or type(other) is float:
                return Vector([x1 * other for x1 in self.aList])
            else:
                raise TypeError("can't multiply sequence of:{0} and {1}".format(type(self), type(other)))
        else:
            if len(self.aList) != len(other.aList):
                raise Exception("Vectors have different size.")
            return Vector([x1 * x2 for x1, x2 in zip(self.aList, other.aList)])

    def __eq__(self, other):
        if type(other) is not Vector:
            raise TypeError("can't check {0} and {1} for equality".format(type(self), type(other)))
        if len(self.aList) != len(other.aList):
            raise Exception("Vectors have different size.")
        for x1, x2 in zip(self.aList, other.aList):
            if x1 != x2:
                return False
        return True

    def __len__(self):
        s = 0
        for x in self:
            s = s + x ** 2
        return sqrt(s)

    def __neg__(self):
        return Vector([-i for i in self.aList])

    def __getitem__(self, i):
        try:
            return self.aList[i]
        except:
            raise IndexError("Vector index out of range")

    def __str__(self):
        return str(self.aList)

if __name__ == '__main__':
    a = Vector([1, 2, 3, 4])

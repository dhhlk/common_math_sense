class Variable:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __add__(self, other):
        return f"{self} + {other}"

    def __radd__(self, other):
        return f"{other} + {self}"

    def __mul__(self, other):
        return f"{other}{self}"

    def __rmul__(self, other):
        return f"{other}{self}"


x = Variable("x")
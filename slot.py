class Class1():
    __slots__ = ['x', 'y', 'a']

    def __init__(self, a, b):
        self.x = a
        self.y = b
        self.a = 100

c1 = Class1(10, 20)

print(c1.x, c1.y)
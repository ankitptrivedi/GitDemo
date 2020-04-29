class Calculator:
    num = 100

    def __init__(self, a, b):
        self.firstnum = a
        self.secondnum = b
        print("Called automatically")

    def getData(self):
        print("This is a method which is a function used in a class")

    def Sum(self):
        return self.firstnum + self.secondnum + self.num


obj = Calculator(2, 2)
obj.getData()
print(obj.Sum())

obj1 = Calculator(4, 5)
obj1.getData()
print(obj1.Sum())

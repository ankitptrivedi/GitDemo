from OopsDemo import Calculator


class ChildImplemen(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 9)

    def getCompData(self):
        return self.num2 + self.num + self.Sum()


obj = ChildImplemen()
print(obj.getCompData())

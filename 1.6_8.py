#
# print((5).__eq__(7))
# print((5).__gt__(7))
# print((5).__le__(7))
# print((50).__ge__(7))
# print((10).__le__(7))
# print((10).__ne__(7))

class Money:
    def __init__(self,value):
        self.value=value
    def __eq__(self, other):
        return self.value==other.value
m1=Money(100)
m2=Money(10)
print(m1==m2)
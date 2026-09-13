#__repr__
class Laptop:
    def __init__(self,brand,cost):
        self.brand=brand
        self.cost=cost
    def __repr__(self): #override__repr__
        return f"{self.brand}->{self.cost}"
l1=Laptop("TUF",75000)
l2=Laptop("HP",80000)
l3=Laptop("DELL",70000)
lap_list=[l1,l2,l3]
print(lap_list)
print(l1) #When __str__ is absent and __repr__ is present and print instance
print(repr(l1)) #L1.__repr__()
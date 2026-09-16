#__hash__()
class Citizen:
    def __init__(self,adhaarnumber,state):
        self.adhaarnumber=adhaarnumber
        self.state=state
    def __hash__(self):  #Method Overriding
        return self.adhaarnumber 
c1=Citizen(1212123,"Karnataka") #instantiation
c2=Citizen(11111,"Delhi")
print(hash(c1))  #calling hashfunction  c1.__hash__()
print(hash(c2))
############################

class Product:
    def __init__(self,productid,name,cost):
        self.p_id=productid
        self.p_name=name
        self.p_cost=cost
    def __hash__(self):
        return self.p_id #choose unique or something no repeated
p1=Product(1,"aaa",30)
p2=Product(2,"BBB",20)
print(hash(p1))
print(hash(p2))
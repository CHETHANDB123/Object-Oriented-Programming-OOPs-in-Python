##Private
class Politician:
    def __init__(self,name,party,funds):
        self.name=name  #public IV
        self.party=party  #public IV
        self.__funds=funds #Private IV

    def __multpily_money(self): #private IM
        print("Politican enter into Real Estate and dumping yards")
    def file_RTI(self): #public IM
        print(self.__funds)  #access private IV inside public IM inside the class
        self.__multpily_money()  #access private IM inside public IM inside the class
p=Politician("Nagraj","vinoothana party",35000000)
# print(p.__funds) #CANNOT access private IV outside the class Directly
# p.__multpily_money()  #CANNOT access private IM outside the class Directly

p.file_RTI() #Access the public IM


####################
class BusinessMan:
    def __init__(self,name,category,profits):
        self.nam=name
        self.category=category
        self.__profit=profits
    def __share_dividend(self):
        print("profit")
    def file_incometax(self):
        print(self.__profit)
        self.__share_dividend()
bm=BusinessMan("chethan","Export",20000000)
bm.file_incometax()
#Instance Method
class Employee:
    def __init__(self,name,id,salary):   #Constructor
        self.name=name
        self.id=id
        self.salary=salary
        
    def display_details(self):
        print(self.name,self.id,self.salary)   #Access IV inside Im using self paramater

    def deduct_salary(self,amount):
        self.salary-=amount #Modify IV inside IM using self parameter
   
e1=Employee("chethan",1,50000)
e2=Employee("surya",2,30000)
e1.display_details()
e2.display_details()
e1.deduct_salary(10000)
print(e1.salary)
print(e1.__dict__)
####################################
class Restrutant:
    def __init__(self,name,loaction):  #Constructor
        self.name=name
        self.loc=loaction
    def display_details(self): #Access
        print(self.name,self.loc)
    def display_modify(self,rename):  #modify
        self.name=rename
r1=Restrutant("aaa","xxxxxxxx")  #r1=object | Call
r1.display_details()
r1.display_modify("BBBB")
r1.display_details()
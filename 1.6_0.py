#__str__()
class Student:
    pass
p=Student()
print(p)   #
Student.__str__(p) #Method
print(p)
################## 
class Pen:
    def __str__(self):
        return "Custom Message"
p1=Pen()
print(p1)  #p1.__str__()
p2=Pen()
print(p2)

######################


#dunder method overriding
#__init__
class Student1:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def __str__(self):  #Override method
        return f"{self.name} -> {self.roll}"
s1=Student1("Sharath",23)
s2=Student1("chethan",1)
s3=Student1("Virat",18)
print(s1)
print(s2)
print(s3)

############################
class Employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def __str__(self):
        return f"{self.name} -> {self.id} -> {self.salary}"
e1=Employee("chethan",1,30000)
e2=Employee("sharath",2,45000)
print(e1)
print(e2)
print(str(e1))
print(str(e2))

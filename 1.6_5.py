#__eq__()
#__init__()
class Employee:
    def __init__(self,eid,name,dept):
        self.eid=eid
        self.name=name
        self.dept=dept
e1=Employee(111,"chethan","developement")
e2=Employee(22,"charn","cybersecurity")
print(e1==e2) #print(e1.__eq__(e2))

#############################
class Employee1:
    def __init__(self,eid,name,dept):
        self.eid=eid
        self.name=name
        self.dept=dept
    def __eq__(self,other):
        if isinstance(other,Employee1):
          return self.eid==other.eid
        #    111==111  True | Duplicate ID and if 2==4 False No Duplicate ID
e1=Employee1(111,"chethan","developement")
e2=Employee1(111,"charn","cybersecurity")
# print(e1==e2) #print(e1.__eq__(e2))
print(isinstance(e1,Employee1))
print(isinstance(10,int))
##################################3
class Employe2:
    def __init__(self,eid,name,dept):
        self.eid=eid
        self.name=name
        self.dept=dept
    def __eq__(self,other):
        if isinstance(other,Employe2):
          return self.eid==other.eid
        return False
        #    111==111  True | Duplicate ID and if 2==4 False No Duplicate ID
e1=Employe2(111,"chethan","developement")
e2=Employe2(111,"charn","cybersecurity")
print(e1==90)
print(e1==e2)

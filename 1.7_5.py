##public
class Employee:
    def __init__(self,name,eid,dept):
        self.name=name  #3 public IV
        self.eid=eid
        self.dept=dept

    def display(self):  #public IM
        print(self.name,self.eid,self.dept)  #access public IV inside the class
e=Employee("arun",22,"management")  #instance
print(e.name)  #access public IV outside the class
e.display()  #access public IM otuside the class
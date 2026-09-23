##Protected
class Student:
    def __init__(self,roll,name,fees):
        self.rool=roll  #public IV
        self.name=name  #public IV
        self._fees=fees #protected IV

    def _pay_fees(self):
        print(f"{self.name} paid {self._fees} to the institution")  #access protected IV inside

class EngineeringStudent(Student):
    def quaterly_installment(self):  #public IM
        self._pay_fees()  #Accesssing the protected IM from the child class    
es=EngineeringStudent(29,"chethan",78000)
es.quaterly_installment()

print(es._fees) #Access protected outside the class

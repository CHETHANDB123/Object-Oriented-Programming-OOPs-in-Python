#Prvate Getter
class Student:
    def __init__(self,name):
        self.name=name #Public IV
        self.__marks=0  #private IV
    def get_marks(self):  #public Getter Method
        return self.__marks  #returning the private data
    
    def set_marks(self,newmarks):  #public setter method
        if newmarks>0 and newmarks<=100: #validation logic
            self.__marks=newmarks   #updation
        else:
            print("Invalid marks entered")
s1=Student("chethan")
# print(s1.get_marks())
s1.set_marks(44)
print(s1.get_marks())

################################

class Patient:
    def __init__(self,name,age):
            self.name=name #Public IV
            self._age=age
            self.__bp=None
    def get_bp(self):  
            return self.__bp
    def set_patient(self,restore_bp):
         if restore_bp>80 or restore_bp<120:
              self.__bp=restore_bp
         else:
            print("sorry")
p1=Patient("virat",30)
# print(p1.get_bp())
p1.set_patient(900)
print(p1.get_bp())
####################################

class BankAccount:
     def __init__(self,name,accnum):
          self.name=name
          self._accnum=accnum
          self.__balance=500
     def get_balance(self):
          return self.__balance
     def deposit(self,amount):
          if amount>0:
               self.__balance+=amount
          else:
               print("Invalid")
     def withdraw(self,amount):
          if amount>0 and amount<=self.__balance:
               print("withdrawing")
          else:
               print("Invalid Balance")
ba=BankAccount("chethan",1211111)
# print(ba.get_balance())
ba.deposit(1000)
print(ba.get_balance())
# print(ba.deposit())
ba.withdraw(2000)
print(ba.get_balance())


      
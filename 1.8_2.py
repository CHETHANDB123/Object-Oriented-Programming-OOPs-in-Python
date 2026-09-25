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
# print(s1.name)
print(s1.get_marks())
# s1.set_marks(44)
# print(s1.get_marks()
# #############################

class Student1:
    def __init__(self,name):
        self.name=name  #public IV
        self.__marks=0  #private IV
        self.__fees=0
    @property
    def marks(self):  #Getter defines the property marks
        return self.__marks
    def fees(self):
        return self.__fees

    @marks.setter     #Setter for thatr property marks
    def marks(self,newmarks):
        if newmarks>0 and newmarks<101:
            self.__marks=newmarks
        else:
            print("Invalid")
    # def fees1(self):

s=Student1("chethan")
print(s.marks)   #Access like a variable Getter method gets called
s.marks=77      #Initialise like a variable Setter method gets called
print(s.marks)
print(s.marks)
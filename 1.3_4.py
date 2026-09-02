###Class Methods 
class Student:
    school="Adarsh vidhalaya"       #classvariable 1
    principal="Gundegowda"      #CV2
    fees=200000      #CV3
    @classmethod
    def increase_fees(cls):
        # print("fees of each student will be increased")
        #  print(cls.fees)   ##access CV inside class method
        cls.fees+=50000   #Modify Cv Inside a class
        print(Student.fees)
    @classmethod
    def display_school(cls):
        print(cls.school)
Student.display_school()
Student.increase_fees()
Student.increase_fees()
Student.increase_fees()   #Access/call class method
print(Student.fees)
##################
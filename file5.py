##Constructor Chaining
class Student:
    def __init__(self,name,roll):
        self.name=name
        self.rool=roll
class SchoolStudent(Student):
    def __init__(self, name, roll,principal):
        super().__init__(name,roll)
        self.principal=principal
s=SchoolStudent("chethan",1,"bbb")
print(s.__dict__)

##############################################
class Person:
    def __init__(self,name,age,gender,nationality):
        self.name=name
        self.age=age
        self.gender=gender
        self.Nationality=nationality
class Citizen(Person):
    def __init__(self,name,age,gender,nationality,citizen_id):
        super().__init__(name,age,gender,nationality)
        self.citizen_id=citizen_id
class refugee(Citizen):
    def __init__(self, name, age, gender, nationality,citizen_id,refugee_id):
        super().__init__(name, age, gender, nationality,citizen_id)
        self.refugee_id=refugee_id
pe=refugee("chethan",22,"male","Indian",3,55)
print(pe.__dict__)
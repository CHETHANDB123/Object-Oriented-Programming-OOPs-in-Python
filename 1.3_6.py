#static method
class Student:
    def __init__(self,name,roll):
        self.name=name  #IV1
        self.roll=roll  #IV2
    @staticmethod               #not dependent on self or cls
    def calculate_percentage(marks,total_marks):  #Static method
        print((marks/total_marks)*100)
Student.calculate_percentage(500,900)
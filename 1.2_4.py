#Class Variable
class Student:
    course="python" #CV1 inside the class
    classroom=201 #CV2
# print(Student.__dict__)
Student.institute="DCL"  #CV3 outside the class
Student.yop=2026
# print(Student.__dict__)
print(Student.institute) #Accessing var outside the class

###########

#Instabce Variable
s1=Student()#instance
s1.name="chethan"  #Iv1
s1.college="AIET"  #IV2
print(s1.__dict__)
s1.college="MIT"  #modify
print(s1.__dict__)
print(s1.name) #access IV using ref



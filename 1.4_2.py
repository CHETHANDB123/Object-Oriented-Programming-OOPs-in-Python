#Single level
class Student:   #Parent class
    def study(self): #IM in parent class    | study= method
        print("every student is expected to study")
class Engineering_student(Student):   #Child Class
    def persent_project(self):   #IM in child class
        print("engineering student are expected to do project")

es=Engineering_student() #instantiation
es.persent_project()  #Using child object ref,access child IM
es.study()   #using child object ref,access parent IM
print(Engineering_student.__mro__)
#####################################
class Developer:
    def delop(self):
        print("i am coder")
class FrontendDeveloper(Developer):
    def front(self):
        print("Design the web page")
df=FrontendDeveloper()
df.front()   #IV=obj_ref
df.delop()

print(FrontendDeveloper.__mro__)

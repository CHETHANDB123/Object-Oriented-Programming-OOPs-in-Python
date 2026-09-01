# 1)Default Constructor
# 2)Custom Constructor         #Non-Parametrized Custom Constructor
#There are no parameters other than 'self', so it is called a non-parameterized constructor.
class Student:
    def __init__(self):   #Constructor/Initialiser  #self refers to current  object invoked
        # print("constructor")
        # print(self)
        self.name="chethan"    #Instance variable
s1=Student()   #obj creation
s2=Student()
s3=Student() 

print(s1)   #Address  
print(s1.name) ## Accesses the instance variable
# print(s1.__dict__)
print(s2.name)      
print(s3.name)


###############################
#Parametrized Custom Constructor
class Students:
    def __init__(self,name,rool,marks):
        self.n1=name
        self.r1=rool
        self.m1=marks
s4=Students("swathi",420,50)
print(s4.__dict__)
s5=Students("sharath",29,100)
print(s5.__dict__)
###

class Actor:
    def __init__(self,name,movie,Industry):
        self.n=name
        self.m=movie
        self.i=Industry
s6=Actor("Prabhas","Bhaubali","Telugu")
s7=Actor("Yash","Toxic","kannad")
print(s6.__dict__)
print(s7.__dict__)
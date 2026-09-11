#__new__
#(object) Empty object
class Pen:
    pass
# p=Pen()
# print(p)

p=Pen.__new__(Pen)  #true constructor , it will go to line 2 
Pen.__init__(p)     #Initailser executes
print(p)

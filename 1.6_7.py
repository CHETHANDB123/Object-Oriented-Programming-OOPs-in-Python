#
class Sample:
    pass
print((5).__add__(7)) #Pre-defined | Inbillt classes 
print((5).__sub__(7))
print((5).__mul__(7))
print((50).__truediv__(7))
print((10).__floordiv__(5))
print((10).__mod__(2))
print((10).__pow__(3))

############
# class Money:  #userdefined class
#     def __init__(self,value):
#         self.value=value
#     def __add__(self, other):  # (m1,m2)
#         return Money(self.value+other.value)
#     def __str__(self):  #convert obj address to value
#         return f"{self.value}"
#     def __sub__(self, other):
#         return self.value-other.value
#     def __mul__(self, other):
#         return self.value*other.value
#     def __truediv__(self, other):
#         return self.value/other.value
#     def __floordiv__(self, other):
#         return self.value//other.value
#     def __mod__(self, other):
#         return self.value%other.value
#     def __pow__(self, other):
#         return self.value**other.value
# m1=Money(100)   #user defined object
# m2=Money(500)
# m3=Money(200)
# m4=Money(10)
# m5=Money(2)
# print(m1+m2+m3)  #print(m1.__add__(m2).__add__(m3))
# print(m2-m1)
# print(m1*m2)
# print(m1/m2)
# print(m2//m3)
# print(m4%m5)
# print(m4**m5)
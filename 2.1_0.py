#Approach=2

# print("Start")
# print(1)
# print(2)
# print(3)
# try:
#     print(5/0) # risky line of code with may raise an exception
# except ZeroDivisionError as e:  #except block refers handling code | ZDE created by PVM =Object
#     print(e) #exception objects message will be shown
# print("End")
# ###############################

# print("Start")
# print(1)
# print(2)
# print(3)
# try:
#     print(d) # risky line of code with may raise an exception
# except NameError as e:  #except block refers handling code | ZDE =Object
#     print("Exception Handeled",e)
# print("End")

##############################
#Approach=3

# print("Start")
# print(1)
# l=[10,20,30,40]
# try:
#     p=int(input("Enter 1st number"))
#     q=int(input("Enter 2nd number"))
#     print(p/q)
#     print(l[q])
# except ValueError as e1:
#     print("Value Error",e1)
# except ZeroDivisionError as e2:
#     print(e2)
# except IndexError as e3:
#     print('Index Error',e3)
# print("End")
#########################3

#Approach=4
# print("Start")
# print(1)
# l=[10,20,30,40]
# try:
#     p=int(input("Enter 1st number"))
#     q=int(input("Enter 2nd number"))
#     print(p/q)
#     print(l[q])
# except(ValueError,ZeroDivisionError,IndexError) as e:
#     print(e)
#print("End")

#######################
#Default Except block

# print("Start")
# print(1)
# l=[10,20,30,40]
# try:
#     p=int(input("Enter 1st number"))
#     q=int(input("Enter 2nd number"))
#     print(p/q)
#     print(l.appond[q])
# except(ValueError,ZeroDivisionError,IndexError) as e:
#     print(e)
# except Exception as e2:
#     print(e2)
# print("End")
#####################

print(2)
try:
    print(2/0)
except Exception as e:  #All 3 Errors are Inherit from Exception , Catching Exception will automatically catch all of them
    print("hello",e)  #e stores actual error message inside a variable named e so we ca print it

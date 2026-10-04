# Normal Execution
print("Start")
print(1)
print(2)
print(3)
print(4)
print(5)
try:
    print(6/0)
except ValueError:
    print("It will not Execute")
except:  #This is the Default Exception handler block
    print("ZerrodivisionError")
print("End")


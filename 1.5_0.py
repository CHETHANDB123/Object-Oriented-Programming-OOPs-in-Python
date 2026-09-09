# from typing_extensions import override
#Method Overriding
class Athlete: #Parent Class
    def Pushups(self):
        print("Waramup pushups 10")
class Wrestler(Athlete): #1)inheritance | Child Class
    # @override
    def Pushups(self):      #2)methodname and para same
            print("50 Diamond pushups for Wreatler")  #3)method Implement
w=Wrestler()
w.Pushups()
print(Wrestler.__mro__)
########################################
# Super()
# from typing_extensions import override
#Method Overriding
class Athlete: #Parent Class
    def Pushups(self):
        print("Waramup pushups 10")
class Wrestler(Athlete): #1)inheritance | Child Class
    # @override
    def Pushups(self):      #2)methodname and para same
            # super().pushups()
            print("50 Diamond pushups for Wreatler")  #3)method Implement
w=Wrestler()
w.Pushups()
print(Wrestler.__mro__)




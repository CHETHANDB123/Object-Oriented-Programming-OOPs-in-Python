#hybrid-level
class player:
    def paly(self):
        print("playing")
class Batman(player):
    def bat(self):
        print("Bating")

class Bowler(player):
    def bowl(self):
        print("Bowling")
class AllRounder(Batman,Bowler):
    def field(self):
        print("Fielding")

all1=AllRounder()
all1.field()
all1.bat()
all1.bowl()
all1.paly()
print(AllRounder.__mro__)

########################
class Employee:
    def emp(self):
        print("I am Employee")
class FrontEndDeveloper(Employee):
    def front(self):
        print("Develop Interfame")
class BackEndDeveloper(Employee):
    def back(self):
        print("i handel the Database")
class FullstackDeveloper(FrontEndDeveloper,BackEndDeveloper):
    def full(self):
        print("I Develop the Web Page")
e1=FullstackDeveloper()
e1.full()
e1.back()
e1.front()
e1.emp()
print(FullstackDeveloper.__mro__)
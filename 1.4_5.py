#Multiple-level
class Batsman:
    def bat(self):
        print("Batting")
class Bowler:
    def bowl(self):
        print("Bowling")
class AllRounder(Batsman,Bowler):
    def field(self):
        print('Fielding')
a1=AllRounder()
a1.field()
a1.bat()
a1.bowl()
print(AllRounder.__mro__)
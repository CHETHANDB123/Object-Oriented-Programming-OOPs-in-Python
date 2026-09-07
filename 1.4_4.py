#Heirarchical-level
class Minister:
    def attend_meeting(self):
        print("Meeting")
class HealthMinister(Minister):
    def education_reform(self):
        print("Announcing the Major results(10th)")
class FinanceMinister(Minister):
    def budget_speech(self):
        print("Planning country's year budget")
class EducationalMinister(Minister):
    def inspect_govtfacilities(self):
        print("Raid the Hotels")
m1=Minister()
m1.attend_meeting()
m2=HealthMinister()
m2.education_reform()
# m2.attend_meeting()
m3=EducationalMinister()
m3.inspect_govtfacilities()
m4=FinanceMinister()
m4.budget_speech()

print(EducationalMinister.__mro__)
print(FinanceMinister.__mro__)
print(HealthMinister.__mro__)
print(Minister.__mro__)
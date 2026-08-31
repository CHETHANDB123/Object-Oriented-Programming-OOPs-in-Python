class MarkerPen: #userdefined class
    'this class is for 10 pen'
    pass
class Mobile: #userdefined class
    pass
pen1=MarkerPen()
print(pen1)
pen2=Mobile()
print(pen2)
 
print(MarkerPen.__dict__) #class dictionary
print(pen1.__dict__) #empty instance dictionary
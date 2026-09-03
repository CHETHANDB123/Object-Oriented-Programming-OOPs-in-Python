#ALL Three types of methods in a single class
class Movie_ticket:
    theater="PVR"  #CV
    gst=0.18
    def __init__(self,seatno,moviename,is_adult):  #IV
        self.seat=seatno
        self.movie=moviename
        self.adult=is_adult
    #Class method
    @classmethod
    def display_cv(cls): #Cm->CV
        print(cls.theater)
        print(cls.gst)
    
    #Instance Method
    def display_iv(self):  #IM->IV
        print(self.seat,self.movie,self.adult)
    #Static Method
    @staticmethod
    def calculate_bill(ticketprice,quantity):
        print("Total Bill :",ticketprice*quantity)
        # total=ticketprice*quantity
        # return total
#creating 1 objects
m1=Movie_ticket("A10","Toxic",True)

#calling class method
Movie_ticket.display_cv()

#call Instance Method
m1.display_iv()

#calling Static Method

total=Movie_ticket.calculate_bill(240,4)
# print("Total Bill:",total)
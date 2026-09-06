#Multi-level
class vehicle:
    def move(self):
        print("moving on a road")
class Bike(vehicle):
    def ride(self):
        print("moto GP ridding")
class ElectricBike(Bike):
    def charge(self):
        print("Charging phone")

v1=ElectricBike()
v1.ride()
v1.charge()
v1.move()
print(ElectricBike.__mro__)
print(Bike.__mro__)
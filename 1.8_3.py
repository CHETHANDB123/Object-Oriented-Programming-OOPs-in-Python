#Abstract Method
from abc import ABC , abstractmethod
class Application(ABC):
    @abstractmethod
    def login(self): #method
        pass
class WebApplication(Application): #Subclass shuld inherit abstract class
    def login(self):            #shuld override all abstract methods of parent class
        print("enter username and pssword")
we=WebApplication()
we.login()

########################

from abc import ABC , abstractmethod
class SuccessfulPerson(ABC):
    @abstractmethod
    def earn_money(self):
        pass
class BussinessMan(SuccessfulPerson):
    def earn_money(self):
        print("you are successful")

sp=BussinessMan()
sp.earn_money()
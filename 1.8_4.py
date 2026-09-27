#I want to define a contarct which the Enforce the child classes to implement then rectangle , square

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def Calculate_area(self):
        pass
class Rectangle(Shape):
    def Calculate_area(self):
        print("length*breadth")
sr=Rectangle()
sr.Calculate_area()

################################3

from abc import ABC, abstractmethod
class Trainer(ABC):
    @abstractmethod
    def train(self):
        pass
class Python_Trainer(Trainer):
    def train(self):     #Method
        print("Mock face to face")
class Sql_Trainer(Trainer):
    def train(self):
        print("LMS Portal")
class Frontend(Trainer):
    def train(self):
        print("Surprise Test")
tr=Python_Trainer()   # Create object
tr.train()           # Call train() method
tr=Sql_Trainer()
tr.train()
tr=Frontend()
tr.train() 
import pickle
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __str__(self):
        return f"{self.name}->{self.salary}"
with open("filehandling/employee.pkl","w+b") as f:
    e=Employee("raju",999900000)
    #bin_data=pickle.dumps(e)
    pickle.dump(e,f)
    #f.write(bin_data)
    f.seek(0)
    #data=f.read()
    eo=pickle.loads(f)
    print(eo)#eo__str__()

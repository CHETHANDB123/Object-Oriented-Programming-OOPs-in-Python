#Class Variable
class job:    #class = keyword  | job=Class Name
    sa=10000   #sa=Class Variable
    company="abc"  #"abc"=value of company 
job.year=2026         #It is Used in all are equal,Dependent | All are below to one Class
job.login="Nine-AM"
print(job.__dict__)

#Instance Variable
s1=job()                #It is Independent | It wil Create Separately each one
s1.name="chethan"       #Belongs to an object/instance
                    	#Created using an object or self
s1.Company="IBM"
s1.Salary=800000
print(s1.__dict__)     
print(s1.Company)

#job → Class name
#job() → Creating an object (instance) of the class
#s1 → Object reference / variable that refers to that object
#Duck Typing
class Zomata:
    def deliver(self):
        print("zomato delivery")
class swigy:
    def deliver(self):
        print("swigy delivery")
class ubereat:
    def deliver(self):
        print("udereat deilvery")
# class Porter:
#     def transport(self):
#         print("porter transport goods/methods")

#########
def process(partner):
    if hasattr(partner,"deliver"):
        partner.deliver()
z=Zomata()
s=swigy()
u=ubereat()

################
print(hasattr(z,"deliver"))
# p=Porter()
l=[z,s,u]
for i in l:
    process(i)
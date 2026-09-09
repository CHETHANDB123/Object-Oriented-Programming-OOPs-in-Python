#Method Overriding
class Minister:
    def address_public(self):
        print("solving Issues")
class FinanceMinister(Minister):
    def address_public(self):
        print("Increase the tax")
mi=FinanceMinister()
mi.address_public()


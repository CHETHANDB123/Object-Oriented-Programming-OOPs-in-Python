#Mutliple Methods / super()
class Whatsapp1:
    def send_message(self):
        print("Single tick message")
class Whatsapp2(Whatsapp1):
    def send_message(self):  #Method
        super().send_message()  #Override
        print("Double tick message")
    def send_audio(self):
        print("1 min audio support")
class Whatsapp3(Whatsapp2):
    def send_message(self):
        super().send_message()
        print("Blue tick message")
    def send_audio(self):
        super().send_audio()
        print("Extar 5 min Support")
    def send_vedio(self):
        print("Support 3 min Vedio")
w3=Whatsapp3()
w3.send_message()
w3.send_audio()
w3.send_vedio()
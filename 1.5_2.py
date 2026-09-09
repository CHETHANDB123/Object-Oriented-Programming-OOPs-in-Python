#2) Super()
# from typing_extensions import override
class Singer:
    def sing(self):
        print("Singing a Song")
class ClassicalSinger(Singer):
    # @override
    def sing(self):
        super().sing()
        print("Classical Singer")

s1=ClassicalSinger()
s1.sing()
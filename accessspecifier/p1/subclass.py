from p1.protection1 import Protection1

class SubClass(Protection1):
    def __init__(self):
        super().__init__()
        print("public_x :", self.public_x)
        print("protected_y :", self._protected_y)
       # print("private_c :", self.__private_c)
        print("---------------------------")
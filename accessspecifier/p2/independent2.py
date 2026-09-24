from p1.protection1 import Protection1


class Independent2:
    def __init__(self):
        self.o=Protection1()
        print("public_x :",self.o.public_x)
        print("protected_y :", self.o._protected_y)
        #  print("private_z :", self.o.__private_z)
        print("----------------------")

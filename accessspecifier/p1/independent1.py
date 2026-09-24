from p1.protection1 import Protection1


class Independent:
    def __init__(self):
        self.o=Protection1()
        print("publioc _x :",self.o.public_x)
        print("protected_y :", self.o._protected_y)
      #  print("private_z :", self.o.__private_z)
        print("----------------------")

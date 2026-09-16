
class Maths1:
    def __init__(self):
        self.x=10
        self.y=5

    def addition(self):
        result=(self.x + self.y)
        print("Addition Result :",result)

    def multiplication(self):
        result=(self.x * self.y)
        print("Multiplication Result :",result)

obj1=Maths1()
print(obj1.x, obj1.y)
obj1.addition()  # 15
obj1.multiplication()  # 50

obj2=Maths1() 
obj2.addition()   # 15
obj2.multiplication()  # 50
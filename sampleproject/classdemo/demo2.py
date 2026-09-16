
class Maths1:
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def addition(self):
        result=(self.a + self.b)
        print("Addition Result :",result)

    def multiplication(self):
        result=(self.a * self.b)
        print("Multiplication Result :",result)

obj1=Maths1(20,5)  
print(obj1.a, obj1.b)  
obj1.addition()
obj1.multiplication() 

obj2=Maths1(15,9)
obj2.addition()
obj2.multiplication()


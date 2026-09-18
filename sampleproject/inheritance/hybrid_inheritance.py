class Maths1:
    def addition(self, x, y):
        result=(x + y)
        print("Addition Result :",result)

class Maths2(Maths1):
    def substration(self, x, y):
        result= (x - y)
        print("Substration Result :",result)

class Maths3(Maths1):
    def division(self, x, y):
        result= (x / y)
        print("Division Result :",result)

class Maths4(Maths3):
    def multiplication(self, x, y):
        result= (x * y)
        print("Multiplication Result :",result)

obj1=Maths2()
obj1.substration(45,15)
obj1.addition(10,40)

obj2=Maths4()
obj2.multiplication(13,10)
obj2.division(60,10)
obj2.addition(40,100)
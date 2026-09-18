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

obj1=Maths2()
obj1.substration(50,20)
obj1.addition(10,30)

obj2=Maths3()
obj2.division(35,7)
obj2.addition(60,30)
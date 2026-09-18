class Maths1:
    def addition(self, x, y):
        result=(x + y)
        print("Addition Result :",result)

class Maths2(Maths1):
    def substration(self, x, y):
        result= (x - y)
        print("Substration Result :",result)

class Maths3(Maths2):
    def division(self, x, y):
        result= (x / y)
        print("Division Result :",result)

obj=Maths3()
obj.division(45,9)
obj.substration(50,10)
obj.addition(45,65)
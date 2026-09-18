class Maths1:
    def addition(self, x, y):
        result=(x + y)
        print("Addition Result :",result)

class Maths2:
    def substration(self, x, y):
        result= (x - y)
        print("Substration Result :",result)

class Maths3(Maths1, Maths2):
    def division(self, x, y):
        result= (x / y)
        print("Division Result :",result)

obj=Maths3()
obj.division(35,7)
obj.substration(60,20)
obj.addition(40,60)
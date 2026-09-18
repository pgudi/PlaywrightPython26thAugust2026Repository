class Maths1:
    def addition(self, x, y):
        result=(x + y)
        print("Addition Result :",result)

class Maths2(Maths1):
    def substration(self, x, y):
        result= (x - y)
        print("Substration Result :",result)

obj=Maths2()
obj.substration(35,10)
obj.addition(50,40)
class Maths:
    @staticmethod
    def addition(x,y):
        result=(x + y)
        print("Addition Result :",result)

    @staticmethod
    def multiplication(x,y):
        result=(x * y)
        print("Multiplication Result :",result)
    

obj=Maths()
obj.addition(20,50)
obj.multiplication(12,10)
print("-----------")
Maths.addition(40,50)
Maths.multiplication(13,9)
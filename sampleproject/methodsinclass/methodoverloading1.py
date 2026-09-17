class Calculation:
    def multiplication(self, **kwargs):
        if(kwargs.get("num2")==None and kwargs.get("num3")==None and kwargs.get("num4")==None):
            result=kwargs.get("num1") * 1
            print("Multiplication Result :",result)
        elif(kwargs.get("num3")==None and kwargs.get("num4")==None):
            result=kwargs.get("num1") * kwargs.get("num2")
            print("Multiplication Result :",result)
        elif(kwargs.get("num4")==None):
            result=kwargs.get("num1") * kwargs.get("num2") * kwargs.get("num3")
            print("Multiplication Result :",result)
        else:
            result=kwargs.get("num1") * kwargs.get("num2") * kwargs.get("num3") * kwargs.get("num4")
            print("Multiplication Result :",result)

obj=Calculation()
obj.multiplication(num1=15)
obj.multiplication(num1=15,num2=4)
obj.multiplication(num1=5,num2=4,num3=5)
obj.multiplication(num1=10,num2=2,num3=3,num4=4)
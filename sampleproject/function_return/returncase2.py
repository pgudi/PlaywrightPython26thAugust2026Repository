# If a function returns a value , the return value you can use within the body of another function
def add(x,y):
    return (x + y)

def sub1(a,b):
    result=(a - b)
    return result

def multiplication():
    v1=add(2,8)
    v2=sub1(35,25)
    result= ( v1 * v2)
    print("Multiplication Result :",result)

multiplication()
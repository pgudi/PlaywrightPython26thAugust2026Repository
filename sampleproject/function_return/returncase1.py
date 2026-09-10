# if a function retuns a value, the same function can use as parameter to another function
def add(x,y):
    return (x + y)

def sub1(a,b):
    result=(a - b)
    return result

def mult(x,y):
    result=(x * y)
    print("Multiplication Result :",result)

# First Appraoch
v1=add(3,7)
v2=sub1(10,5)
mult(v1,v2)
# Second Approach
mult(add(12,7), sub1(20,10))
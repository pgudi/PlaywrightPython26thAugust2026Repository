# Variable Length of Parameters using *args

def sum_of_number(*args):
    sum=0
    for num in args:
        sum=sum+num
    print("Sum of Numbers :",sum)

sum_of_number(45)
sum_of_number(4,5)
sum_of_number(4,5,6)
sum_of_number(4,5,6,7)
sum_of_number(4,5,6,7,8)

print("---------------------------")
def multiply_numbers(*args):
    result=1
    for num in args:
        result=result * num
    print("Multiplication Result :",result)

multiply_numbers(10,2)
multiply_numbers(1,2,3)
multiply_numbers(4,5,6,7)
multiply_numbers(4,5,6,7,8)
# Case 3: Write function to find factorial of a given number

def find_factorial(num):
    fact=1
    for i in range(1, num+1):
        fact=fact * i
    print("Factorial of number ",num," is ",fact)


find_factorial(4)
find_factorial(5)
find_factorial(6)
# Example2: Write a function to validate the given number prime
def isPrimeNumber(number):
    flag=0
    for i in range(2, number):
        if(number % i ==0):
            flag=flag+1
            break

    if(flag==0):
        return True
    else:
        return False

# Case 1: Validate the given numebr
v1=isPrimeNumber(11)
print("Prime Number :",v1)

# Case 2: find count of prime numbers in between 10 to 50
count=0
for i in range(10,51):
    if(isPrimeNumber(i)==True):
        count=count+1
print("Count of Prime Numbers in betwen 10 to 50 :",count)

# Case 3: display Prime numbers in between 50 to 75
for i in range(50, 76):
    if(isPrimeNumber(i)==True):
        print(i, end=" ")
print()
# Case 4: Fidn sum of Prime numebrs i nbetween 25 to 50
sum=0
for i in range(25,51):
    if(isPrimeNumber(i)==True):
        sum=sum+i
print("Sum of Prime Numbers 25 to 50 :",sum)

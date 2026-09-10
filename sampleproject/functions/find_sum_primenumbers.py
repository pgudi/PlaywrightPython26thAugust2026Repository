
# Case 7: Write a program to find the sum of prime numbers in between 50 to 100

def find_sum_prime_numbers(start,end):
    sum=0
    for number in range(start, end+1):
        flag=True
        for i in range(2,number):
            if(number % i ==0):
                flag=False
                break
        if(flag==True):
            sum=sum+number
    print("Sum of Prime Number in betweeen ",start," to ",end, " is ",sum)

find_sum_prime_numbers(50,100)
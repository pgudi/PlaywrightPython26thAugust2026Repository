# Write a program to print count of prime numbers in between 10 to 50
count=0
for p in range(10,51):
    flag=True
    for q in range(2,p):
        if(p % q ==0):
            flag=False
            break
    if(flag==True):
        count=count+1
print("Count of Prime Numbers in betweeen 10 to 50 :",count)
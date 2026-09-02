# Write a program to Print prime number in between 10 to 50?

for i in range(10,51):
    flag=0
    for j in range(2,i):
        if(i % j ==0):
            flag=flag+1
            break
    if(flag==0):
        print(i, end=" ")
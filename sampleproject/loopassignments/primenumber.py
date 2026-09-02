# 11) Write a program to verify the given number is Prime or Not
'''
the number should be divisibl by 1 and itself ,that represents prime number
num=9
2,3,4,5,6,7,8
num % (2,3,4,5,6,7,8)

'''
num=17
flag=True
for i in range(2, num):
    if(num % i ==0):
        flag=False
        break

if(flag==True):
    print(num," is a Prime Number")
else:
    print(num," is not a Prime Number")




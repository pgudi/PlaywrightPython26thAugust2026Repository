# 13) Write a program to display sum of even and odd numbers in between 1 to 500?
'''

step 1: Make sure whether you can print numbers 1 to 500
Step 2: In between 1 to 500 print even numbers & odd numbers
Step 3: find sum of even number & sum of odd numbers

'''
evensum=0
oddsum=0
for i in range(1,501):
    if(i % 2 ==0):
        evensum=evensum+i
    else:
        oddsum=oddsum+i
print("Sum of Even numbers in between 1 to 500 :",evensum)
print("Sum of Odd numbers in between 1 to 500 :",oddsum)    

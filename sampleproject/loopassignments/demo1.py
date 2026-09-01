# Write a program to display count of numbers in between 1 to 100 which hare divisible by 8?
'''
 step 1: first make sure whether you can print numebrs 1 to 100
 Step 2: print numebrs in between 1 to 100 which are divisiabel by 8
 Step 3: find counto f numbers for step 2
'''
count=0
for i in range(1, 101):
    if(i % 8 ==0):
        count=count+1
print("Count of Numbers :",count)
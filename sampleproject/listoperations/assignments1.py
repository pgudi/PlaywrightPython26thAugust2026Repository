# 1. Programmatically add odd numbers in between 20 to 40 in to a list and display the numbers which are divisible by 3
'''
 step 1: make sure you can print numebrs 20 to 40
 Step 2: from step 1 print only odd numebrs
 Step 3: Create a list and add all odd numebrs on it
 Step 4: Validate list and display numbers which are divisible by 3
'''
odd =[]
for i in range(20,41):
    if(i % 2 ==1):
        odd.append(i)
print(odd)
# print numebrs which are divisible by 3
for item in odd:
    if(item % 3 ==0):
        print(item)

        
# 2. Programmatically add numbers in between 1 to 100 which are divisible by 9
'''
step 1: print numebrs 1 to 100
Step 2: from step 1 display numebrs which are divisible by 9
Step 3: add ste p2 numebrs into a list
step 4: Print a new list
'''
newlist=[]
for i in range(1, 101):
    if(i % 9 ==0):
        newlist.append(i)

print(newlist)

print("--------------------------------------------")
# List Comprehension:

newlist2=[i for i in range(1,101) if(i % 9 ==0) ]
print(newlist2)

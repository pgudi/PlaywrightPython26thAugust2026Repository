# Case 2: Write a function to return a Integer list from a function.
def get_integer_list():
    new_list=[x for x in range(1,11)]
    return new_list

# Case 1 : display the return value
elements = get_integer_list()
print(elements)
# Case 2: find sum of All Elements in a list
sum=0
for i in range(1, len(elements)+1):
    sum=sum+i
print("Sum of All Elements :",sum)
# Case 3: Print first half of teh Elements
half_elements=[x for x in range(1, int(len(elements)/2)+1)]
print(half_elements)
# Case 4: Print Second Half of Eleemnts
second_half_eleemnts=[x for x in range(int(len(elements)/2)+1, len(elements)+1) ]
print(second_half_eleemnts)
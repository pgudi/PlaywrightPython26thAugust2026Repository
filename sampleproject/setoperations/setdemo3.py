# Case 3: Set Operations Union, Intersect, Difference, Symmetric Difference.
A ={1,2,3,4}
B={3,4,5,6,7}

# Union Operation : It does not provide duplicate Elements
print("A UNION B :", (A | B))
# Intersect Operation: It provides common elements from both the sets
print("A INTERSECT B :",(A & B))
# Minus Operation: It provides Elements from First Set , the same which are not available in second set
print(" A MINUS B :",(A - B))
print(" B MINUS A :",(B - A))
# Symetric Difference : Inverse of Intersect operation
print("A SYMETRIC DIFFERENCE B :", (A ^ B))
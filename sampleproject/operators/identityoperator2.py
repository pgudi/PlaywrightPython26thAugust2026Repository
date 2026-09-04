# Identity operator on List
a=[10,20,30]
b=[10,20,30]
print(a is b)
print(a == b)
print("---------------------")
c=[10,20,30]
d=[10,20,30]
x=c
print(c is d)
print(c is x)
print(x is c)
# is not operator
print(c is not d)
print(c is not x)
# split -> This function splits teh string based on delimiter
str1="Mango,apple,Banana,Orange"
print(str1.split(","))
print("-------------------------")
# splitlines -> This function splits the string based on delimiter
str2='''It is a book
It is on the table
It has many topics on history
'''
print(str2.splitlines())
print("-------------------------")
#lstrip -> It removes blank space on left side
str3="   WELCOME   "
print("Before lstrip , The number of Characters :",len(str3))
print("After lstrip , The number of Characters :",len(str3.lstrip()))
print("-------------------------")
#rstrip -> It removes blank space on right side
str3="   WELCOME   "
print("Before rstrip , The number of Characters :",len(str3))
print("After rstrip , The number of Characters :",len(str3.rstrip()))
print("-------------------------")
#strip -> It removes blank space both sides
str4="   WELCOME   "
print("Before strip , The number of Characters :",len(str4))
print("After strip , The number of Characters :",len(str4.strip()))
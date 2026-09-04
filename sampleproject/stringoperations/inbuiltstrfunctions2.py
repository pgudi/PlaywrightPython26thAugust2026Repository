# Starts with - It verifies beginning of teh string
str1="It is a new palace"
print(str1.startswith("It"))   # True
print(str1.endswith("palace"))  # True
print("-----------------------------------------")
# find -> Find the position of the string or character from Left to Right
str2="It is a book, It is on teh table, it is a new book"
print(str2.find("is"))  # 3
print(str2.find("is",4))  # 17

print("-----------------------------------------")
# rfind -> Find the position of the string or character from Right to Left
str3="It is a book, It is on the table, it is a new book"
print(str3.rfind("is"))
print("-----------------------------------------")
# index  -> Find the position of the string or character from Left to Right
str4="It is a book, It is on teh table, it is a new book"
print(str4.index("is"))  # 3
print(str4.index("is",4))  # 17
print("-----------------------------------------")
# rindex -> Find the position of the string or character from Right to Left
str5="It is a book, It is on the table, it is a new book"
print(str5.rindex("is"))
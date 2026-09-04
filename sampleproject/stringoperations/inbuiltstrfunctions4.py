#islower -> It provides True , if string lower case
str1="sgtesting"  
print(str1.islower())  # True
print("--------------------")
#isupper -> it provides True, if string is upper case
str2="SGTESTING"
print(str2.isupper())  #True
print("--------------------")
#isalph  -> it provides True, if string is alphabetic
str3="sgtest"
print(str3.isalpha())  # True
print("--------------------")
#isalnum  -> it provides True, if string is alpha numaric
str4="sgtest123"
print(str4.isalnum())  # True
print("--------------------")
#istitle  -> it provides True, if the given string, each word first character is in uppercase
str5="We Are Students"
print(str5.istitle())  # True
print("--------------------")
# isspace -> It providesTrue, it string has space
str6=" "
print(str6.isspace())  # True
str7=""
print(str7.isspace())  # False
print("--------------------")
# isdigit -> It provides True, It string has digits
str8="1234" 
print(str8.isdigit())  #True
print("--------------------")
# isnumaric -> It provides True, It string has numbers
str9="1234" 
print(str9.isnumeric())  #True
print("--------------------")
# isdecimal -> It provides True, It string has decimal
str11="12.45" 
print(str11.isdecimal())  #True
print("--------------------")
# Inbuilt Functions
set1={"Apple","Mangp",100,300,"Lotus","Camel",True, False,12.75}
print(set1)
print("----------------")
# copy -> It copies elements and create a new set
elements = set1.copy()
print(elements)
print("----------------")
# pop -> It remove Elements
elements.pop()
print(elements)
elements.pop()
print(elements)
elements.pop()
print(elements)
print("----------------")
# Remove -> It removes Elements based on Element name
print(set1)
set1.remove("Camel")
print(set1)
print("----------------")
# Clear -> This function clears elements in a set
print(set1)
print(set1.clear())


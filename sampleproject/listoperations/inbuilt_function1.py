# Declare a List
cities = ["Mysore","Hassan",45,100,True,10.75,False,"Sira"]

# Extend - > We can add one more list into teh existing list
states=["Karnataka","Kerala","Tamilandu","Maharstra"]
cities.extend(states)
# Print the cities
print(cities)

# index -> It find teh location of teh element [index of the Element]
print(cities.index("Sira"))

# copy List -> it copies teh existing list and it return a copied list
newcities=cities.copy()
print(newcities)

# reverse -> It reverses the Elements in the List
newcities.reverse()
print(newcities)

# sort  -> It sorts the Elements in the List
numbers = [40,90,10,50,20,50,30,50,70]
numbers.sort()
print(numbers)

# count -> It provides the count of duplicate Element
print(numbers.count(50))

# Clear - >It removes all Elements and make it as empty list
numbers.clear()
print(numbers)
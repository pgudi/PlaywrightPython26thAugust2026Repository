# Declare a List
cities = ["Mysore","Hassan",45,100,True,10.75,False,"Sira","Mysore","Hassan"]
print(cities)
# Remove Elements
cities.remove(True)
print(cities)
cities.remove(10.75)
print(cities)
cities.remove("Mysore")
print(cities)
# Remove All Elements
del cities[2]
print(cities)
# Remove entire List
del cities
print(cities)
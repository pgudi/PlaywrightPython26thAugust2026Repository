# Case 11: What is functionality of popitem in dictionary
customers ={
    "customername":"Lenovo Services",
    "emailid":"services@lenovo.com",
    "location":"Bangalore",
    "feeback":"Positive",
    "description":"It is for Testing Purpose"
}

print(customers)
# Apply popitem
v1=customers.popitem()
print(v1)
print(customers)

# Clear all Keys and values
customers.clear()
print(customers)
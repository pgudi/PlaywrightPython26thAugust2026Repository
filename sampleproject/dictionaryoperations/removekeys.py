# Case 10: How to Remove Specific key from Dictionary
customers ={
    "customername":"Lenovo Services",
    "emailid":"services@lenovo.com",
    "location":"Bangalore",
    "feeback":"Positive",
    "description":"It is for Testing Purpose"
}
# Read Value
v1=customers.get("description")
print(v1)
# pop method
v2=customers.pop("description")
print(v2)
# Read Value
v3=customers.get("description")
print(v3)

if(customers.get("country")==None):
    customers["country"]="India"

print(customers)
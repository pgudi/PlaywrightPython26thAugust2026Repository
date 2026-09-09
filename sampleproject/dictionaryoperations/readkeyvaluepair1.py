# Case 5: Read Key and value pair together
customers ={
    "customername":"Lenovo Services",
    "emailid":"services@lenovo.com",
    "location":"Bangalore",
    "feeback":"Positive"
}

# Read Key and alue Together
for x,y in customers.items():
    print(x, "-->",y)
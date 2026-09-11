# Variable Length of Parameters using **kwargs

def display_product_details(**kwargs):
    for k,v in kwargs.items():
        print(k, " --> ",v)
    print("--------------")


display_product_details(prodname="Lenovo Laptop")
display_product_details(prodname="Lenovo Laptop",price=3400)
display_product_details(prodname="Dell Desktop",price=4400, quantity=250)
display_product_details(prodname="Mother Board",price=4900, quantity=100,brand="Intel Corp")
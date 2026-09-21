class Product:
    def __init__(self, pname):
        self.prodname=pname
        print("super Class Variable:",self.prodname)

    
class PurchaseOrder(Product):
    def __init__(self,pname1,pname2):
        super().__init__(pname1)
        self.prodname=pname2
        print("Sub Class Variable:",self.prodname)



# Execute
obj=PurchaseOrder("Lenovo Laptop","Dell Desktop")


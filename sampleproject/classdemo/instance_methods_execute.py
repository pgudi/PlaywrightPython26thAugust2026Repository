
class Customer:

    def show_customer_name(self, custname):
        print("Customer Name ",custname)

    def show_customer_emailId(self, emailid):
        print("Customer Email Id :",emailid)

    def show_customer_location(self, location):
        print("Customer Location :",location)

obj=Customer()
obj.show_customer_name("Lenovo Servies")
obj.show_customer_emailId("info@lenovo.com")
obj.show_customer_location("California")
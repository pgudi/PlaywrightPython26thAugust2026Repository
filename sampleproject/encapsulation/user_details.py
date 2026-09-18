
class Users:
    def __init__(self):
        self.__username=""
        self.__password=""
        self.__emailid=""

    def set_username(self, username):
        self.__username=username

    def set_password(self,password):
        self.__password=password

    def set_emailid(self, emailid):
        self.__emailid=emailid

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_emailid(self):
        return self.__emailid

obj=Users()
obj.set_username("Santosh")
obj.set_password("India@123")
obj.set_emailid("santosh@sg.com")
print(obj.get_username())
print(obj.get_password())
print(obj.get_emailid())
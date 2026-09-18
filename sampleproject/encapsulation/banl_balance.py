
class Bank:
    def __init__(self, balance):
        self.__balance=balance

    def deposit(self, amount):
        if(amount > 0):
            #self.__balance=self.__balance+amount
            self.__balance+=amount

    def get_balance(self):
        return self.__balance

obj=Bank(4000)
obj.deposit(5000)
print(obj.get_balance())
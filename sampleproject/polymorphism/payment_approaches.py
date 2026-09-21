class Payment:
    def pay(self):
        print("The Payment method has started")

class GooglePay(Payment):
    def pay(self):
        print("The Payment method has started using Google Pay")

class PhonePe(Payment):
    def pay(self):
        print("The Payment method has started using PhonePe")

class NetBanking(Payment):
    def pay(self):
        print("The Payment method has started using NetBanking")

payment=Payment()
payment.pay()

googlepay=GooglePay()
phonepe=PhonePe()
netbanking=NetBanking()

payment=googlepay
payment.pay()

payment=phonepe
payment.pay()

payment=netbanking
payment.pay()
"""                                       О.О.П. - ОБЬЕКТНО ОРИЕНТИРОВАННОЕ ПРОГРАММИРОВАНИЕ                                                            """
"""                                                          ПОЛИМОРФИЗМ                                                                                """

# num1 = "fsd"
# num2 = "ads"

# print(num1 + num2)

# num3 = 1
# num4 = 2

# print(num1 + num2)

class PaymentMethod:
    def pay(self, amount):
        pass
class CreditCard(PaymentMethod):
    def pay(self, amount):
        return F"Сумма {amount}, оплачивается по кредитной карте"
class PayPal(PaymentMethod):
    def pay(self, amount):
        return F"Сумма {amount}, оплачивается по PayPal"
class BankTransfer(PaymentMethod):
    def pay(self, amount):
        return F"Сумма {amount}, оплачивается по банковскому переводу"
    
payments = [CreditCard(),PayPal(),BankTransfer()]

for payment in payments:
    print(payment.pay(input('Введите сумму: ')))
    
    
    
    
"""                                                               ГИТХАБ                                                                                """





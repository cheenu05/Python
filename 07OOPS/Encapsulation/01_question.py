# ✅ Q2: Simple Encapsulation
# Ek class Account banao:
# private variable: __balance
# methods:
# deposit(amount)
# get_balance()
# 👉 Rule:
# Balance direct access allowed nahi
# Sirf method se hi change / read ho


class Account:
    def __init__(self):
        self.__balance = 0
    
    def deposit(self , amount):
        self.__balance += amount
    
    def get_balance(self):
        return f"Your account balance is : {self.__balance}"
    

acc = Account()
acc.deposit(10000)
print(acc.get_balance())
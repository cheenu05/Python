# 🧩 Mini Project: Payment Gateway System (OOP Based)
# 🎯 Goal
# Ek aisa system banana jisme:
# User payment method choose kare
# Backend ko sirf pay() call karna pade
# Internals secure rahein
# Naye payment methods easily add ho sakein
# 👉 Matlab Abstraction + Encapsulation + Inheritance + Polymorphism = FULL USE 🔥

# Abstraction class

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

# Inheritance & Encapsulation

class UPI(Payment):
    def __init__(self, upi_id):
        self.__upi_id = upi_id   # encapsulated

    def pay(self, amount):
        print(f"₹{amount} paid using UPI ID {self.__upi_id}")

    # Card

class Card(Payment):
    def __init__(self, card_no, cvv):
        self.__card_no = card_no
        self.__cvv = cvv   # sensitive data

    def pay(self, amount):
        print(f"₹{amount} paid using Card ending {self.__card_no[-4:]}")

    # Wallet 

class Wallet(Payment):
    def __init__(self, balance):
        self.__balance = balance

    def pay(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} paid using Wallet. Remaining balance: ₹{self.__balance}")
        else:
            print("Insufficient wallet balance")


# Polymorphism

def process_payment(payment_method, amount):
    payment_method.pay(amount)




upi = UPI("lakshya@upi")
card = Card("1234567812345678", "123")
wallet = Wallet(1000)

process_payment(upi, 500)
process_payment(card, 700)
process_payment(wallet, 300)



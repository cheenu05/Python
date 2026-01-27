# 2️⃣ Mini ATM System 🏧
# Input:
# balance
# withdraw amount

# Conditions:
# amount ≤ balance → "Transaction Successful"
# amount > balance → "Insufficient Balance"
# amount ≤ 0 → "Invalid Amount"

balance = 10000 
print(balance)
amount = int(input("enter your withdraw amount: "))

if amount <= 0 :
    print("invalid Amount") 
    exit()
elif amount <= balance :
    print("Transaction Successful")
elif amount > balance :
    print("Insufficient Balance")


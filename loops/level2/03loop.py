# 8️⃣ Reverse a number using a loop.
# Example: 1234 → 4321


number = input("enter your number")
reverse =""

for i in number:
    reverse = i + reverse

print(reverse)
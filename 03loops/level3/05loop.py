# 1️⃣5️⃣ Check if a number is a palindrome using a loop.
# Example: 121 → Palindrome

# A palindrome number is a number that reads the same forwards and backward

number = input("enter your number => ")
reverse =""

for i in number:
    reverse = i + reverse

if number == reverse:
        print("The given number is palindrom" , number)
else:
        print("Not a palindrom")

print("the reverse of given number => ", reverse)



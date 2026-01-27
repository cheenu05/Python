# 6️⃣ Find the factorial of a number using a loop.

print("Find the factorial of a number")
number = int(input("enter the number: "))

total = 1

for i in range(1,number+1):
    total = total *i

print("the factorial of given number is => ",total)
# 1️⃣3️⃣ Find the sum of even and odd numbers separately from 1 to n.

number = int(input("enter your number => "))

even = 0
odd = 0

for i in range(1 , number+1):
    if i % 2 == 0 :
       even += i
    else:
       odd += i

print("The sum of all even number is => ",even)
print("The sum of all odd number is => ",odd)
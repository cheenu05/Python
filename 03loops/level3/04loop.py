# 1️⃣4️⃣ Print the Fibonacci series up to n terms.

n = int(input("enter your number => "))

f1, f2 = 0, 1

if n < 1:
        print("enter valid num")
    
print(f1, end=" ")

for i in range(1, n):
        print(f2, end=" ")
        next_fibonacci = f1 + f2
        f1, f2 = f2, next_fibonacci
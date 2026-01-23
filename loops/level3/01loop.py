# 1️⃣1️⃣ Check whether a number is prime or not using a loop.

number = int(input("enther your number => "))

if number <= 1:
    print("not a prime number")
else:
    for i in range(2,number):
        if number % i == 0:
            print("not a prime number")
            break
    else:
            print("prime number")
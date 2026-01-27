# Number Type Detector
# Number input lo aur batao:
# single digit / double digit / multi digit
# even or odd
# Ek input, multiple outputs 💥

number = input("enter your number: ")
actualNumber = int(number)
count = len(number)
print(count)

if count == 1 and actualNumber % 2 == 0:
    print("Even single digit")
elif count == 2 and actualNumber % 2 == 0: 
    print("Even double digit")
elif count > 2 and actualNumber % 2 ==0:
    print("Even muliple digit")
elif count == 1 and actualNumber % 2 != 0:
    print("Odd single digit number")
elif count == 2 and actualNumber % 2 != 0 :
    print("Odd double digit number")
elif count > 2 and actualNumber % 2 != 0:
    print("Odd multiple digit number")


# better readability code

#     number = input("enter your number: ")
# actualNumber = int(number)

# digit_count = len(number)

# if digit_count == 1:
#     digit_type = "single digit"
# elif digit_count == 2:
#     digit_type = "double digit"
# else:
#     digit_type = "multiple digit"

# if actualNumber % 2 == 0:
#     print(f"Even {digit_type}")
# else:
#     print(f"Odd {digit_type}")

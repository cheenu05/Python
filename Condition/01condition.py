#1️⃣ Number Triangle Judge 🔺

# Input: 3 numbers
# Check karo:

# kya triangle ban sakta hai ya nahi
# Rule: sum of any two sides > third side

# 👀 Real maths + logic combo 

numberOne = int(input("enter your number: ")) 
numberTwo = int(input("enter your second number: "))
numberThree = int((input("enter your third number: ")))

if numberOne+numberTwo > numberThree and numberOne+numberThree >numberTwo and numberTwo+numberThree > numberOne:
    print("triangle formed")
else:
    print("not a triangle")

# ik question h ke is program me any 2 value equal honi chaheye tabhi traingle banega

# aur is question ke ye ptaa lga ke triangle 3 equal side wale toh hote he h but aur bhee types hoti h triangle ke 

# 1 : => A scalene triangle is a triangle where all three sides have different lengths, and consequently, all three interior angles have different measures, summing to 180°

#2 : => An isosceles triangle is a triangle with at least two sides of equal length

#3 : => An equilateral triangle is a triangle with all three sides of equal length


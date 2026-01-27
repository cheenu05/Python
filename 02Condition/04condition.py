# 10️⃣ Loan Eligibility Checker 💰
# Input:
# salary
# credit score
# Rules:
# salary ≥ 30,000 AND score ≥ 750 → Approved
# salary ≥ 30,000 AND score < 750 → Review
# else → Rejected
# Logical operators ka full use 🔥

print("Loan Eligibility Checker")
print("Your Salary should be 30000/- minimum")
salary = int(input("Enter your Salary:"))
creditScore = int(input("Enter your Credit Score:"))

if salary >= 30000 and creditScore >= 750 :
    print("Your are Eligible for the process of loan")
elif salary >= 30000 and creditScore < 750:
    print("Your score is average & Your profile is under Review")
else :
    print("Rejected")

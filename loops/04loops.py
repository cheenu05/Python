# 4️⃣ Print all characters of a string one by one.

name = "lakshya"

for i in name:
    print(i)


# 🔍 Your Confusion (Very Valid)
# You thought:
# String is immutable
# Immutable objects behave like int
# int is not iterable
# So maybe string also needs range()

# this program work perfectly : WHY?

# ✅ Core Truth (Important Line)
# Immutability has NOTHING to do with iterability.


# 🧠 Two Different Concepts (Never mix them)
# 1️⃣ Iterability
# 👉 Can Python loop over it?
# 2️⃣ Immutability
# 👉 Can its value be changed in memory?
# They are independent concepts.

# 🧩 Why int is NOT iterable
# num = 5
# for i in num:   # ❌ ERROR
#     print(i)

# Reason:
# int represents one single value
# It does NOT contain multiple elements
# No __iter__() method
# 👉 So Python says: “Bro… what should I loop over?” 🤷‍♂️

# 🧩 Why string IS iterable
# name = "lakshya"

# Because string work as List
# thats why : Python creates an iterator over characters
# One character at a time
# No modification, only reading

# 🔥 Important Clarification (THIS is gold)

# Strings behave like sequences (like lists) for iteration,
# but behave like integers for modification (immutability).

# 😈 Dual personality unlocked.



# 🎯 Interview Power Answer (Say this)

# “Strings are immutable but iterable.
# Immutability prevents modification, not iteration.
# Python allows looping over a string because it is a sequence of characters.”

# 🔥 This answer = solid fundamentals.
# 😄 Fun Way to Remember
# Iterable → “Can I walk over it?” 🚶‍♂️
# Immutable → “Can I change it?” ✋
# String:
# 🚶‍♂️ YES
# ✋ NO
# Int:
# 🚶‍♂️ NO
# ✋ NO 😆



# 🚀 You’re thinking like a real dev now
# This doubt shows:
# You understand memory
# You understand references
# You’re not afraid to question behavior
# Next 🔥 topics you’re READY for:
# enumerate() with strings
# String slicing & memory
# Why strings are hashable (dictionary keys)
# Generator vs string iteration
# Bol bhai 😄
# Next confusion ka lock todte hain 🔓🐍
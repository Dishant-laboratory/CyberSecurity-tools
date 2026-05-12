import re

password = input("Enter password to check: ")

score = 0

# check length
if len(password) >= 8:
    score += 1
if len(password) >= 12:
    score += 1

# check for uppercase
if re.search(r'[A-Z]', password):
    score += 1

# check for lowercase
if re.search(r'[a-z]', password):
    score += 1

# check for numbers
if re.search(r'[0-9]', password):
    score += 1

# check for special characters
if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
    score += 1

# print strength
if score <= 2:
    print("Password is WEAK")
elif score <= 4:
    print("Password is MODERATE")
else:
    print("Password is STRONG")

print(f"Score: {score}/6")
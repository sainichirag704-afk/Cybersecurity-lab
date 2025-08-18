import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    if len(password) >= 8:
        strength += 1
    if re.search("[a-z]", password):
        strength += 1
    if re.search("[A-Z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    if strength == 5:
        remarks = "Strong Password 💪"
    elif 3 <= strength < 5:
        remarks = "Moderate Password ⚠️"
    else:
        remarks = "Weak Password ❌"

    return remarks

# Test
password = input("Enter a password: ")
print(check_password_strength(password))

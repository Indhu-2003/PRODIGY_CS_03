import re

def password_strength(password):
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*()\-_=+{};:,<.>/?\|`~\[\]]', password))

    score = length * 4
    if has_upper:
        score += 4
    if has_lower:
        score += 4
    if has_digit:
        score += 4
    if has_special:
        score += 6

    if length >= 8 and (has_upper or has_lower) and has_digit and has_special:
        return "Strong"
    elif length >= 6 and (has_upper or has_lower) and has_digit:
        return "Moderate"
    else:
        return "Weak"

password = input("Enter your password: ")
strength = password_strength(password)
print(f"Password strength: {strength}")

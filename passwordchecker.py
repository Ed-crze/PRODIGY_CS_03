import re
import random
import string

def check_length(password):
    return len(password) >= 8

def check_uppercase(password):
    return bool(re.search(r"[A-Z]", password))

def check_lowercase(password):
    return bool(re.search(r"[a-z]", password))

def check_digit(password):
    return bool(re.search(r"\d", password))

def check_special_char(password):
    return bool(re.search(r"[\W_]", password))

def check_password(password):
    if not check_length(password):
        return "Password must be at least 8 characters long."
    if not check_uppercase(password):
        return "Password must contain at least one uppercase letter."
    if not check_lowercase(password):
        return "Password must contain at least one lowercase letter."
    if not check_digit(password):
        return "Password must contain at least one digit."
    if not check_special_char(password):
        return "Password must contain at least one special character."
    return "Password is strong."

def suggest_improvements(password):
    suggestions = []
    if not check_length(password):
        suggestions.append("Make it at least 8 characters long.")
    if not check_uppercase(password):
        suggestions.append("Add at least one uppercase letter.")
    if not check_lowercase(password):
        suggestions.append("Add at least one lowercase letter.")
    if not check_digit(password):
        suggestions.append("Add at least one digit.")
    if not check_special_char(password):
        suggestions.append("Add at least one special character.")
    return suggestions

def generate_strong_password():
    length = 12
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

# Example usage
password = input("Enter your password: ")
result = check_password(password)
print(result)

if result != "Password is strong.":
    improvements = suggest_improvements(password)
    print("Suggestions to improve your password:")
    for suggestion in improvements:
        print(f"- {suggestion}")

print(f"Generated strong password: {generate_strong_password()}")
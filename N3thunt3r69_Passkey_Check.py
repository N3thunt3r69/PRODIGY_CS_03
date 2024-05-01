import re

def check_password_strength(password):
    # Minimum length check
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."

    # Presence of uppercase letters
    if not any(char.isupper() for char in password):
        return "Weak: Password should contain at least one uppercase letter."

    # Presence of lowercase letters
    if not any(char.islower() for char in password):
        return "Weak: Password should contain at least one lowercase letter."

    # Presence of numbers
    if not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one number."

    # Presence of special characters
    if not re.search(r'[!@#$%^&*()_+{}|:"<>?`\-=[\];\',./]', password):
        return "Weak: Password should contain at least one special character."

    return "Strong: Password meets all criteria."

if __name__ == "__main__":
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(strength)

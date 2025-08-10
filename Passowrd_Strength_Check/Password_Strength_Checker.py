import re

def check_password_strength(password):
    # Check minimum length
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter"
    
    # Check for lowercase letters
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter"
    
    # Check for digits
    if not re.search(r'[0-9]', password):
        return False, "Password must contain at least one digit"
    
    # Check for special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character"
    
    return True, "Password is strong"

def main():
    print("Password Strength Checker")
    print("------------------------")
    password = input("Enter a password to check: ")
    
    is_strong, message = check_password_strength(password)
    
    if is_strong:
        print("\nSuccess: ", message)
    else:
        print("\nWeak password: ", message)
        print("A strong password should:")
        print("- Be at least 8 characters long")
        print("- Contain both uppercase and lowercase letters")
        print("- Include at least one digit")
        print("- Include at least one special character (e.g., !, @, #, $, %)")

if __name__ == "__main__":
    main()
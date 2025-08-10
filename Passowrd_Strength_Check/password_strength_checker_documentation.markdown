# Password Strength Checker Documentation

## Overview
The `password_strength_checker.py` Python script is designed to evaluate the strength of a user-provided password based on specific criteria. It checks for minimum length, presence of uppercase and lowercase letters, digits, and special characters. The script provides feedback on whether the password is strong or weak, along with guidance on how to improve weak passwords. It is a simple, beginner-friendly tool suitable for use in security-related applications or as a learning exercise.

## Features
- Validates passwords against the following criteria:
  - Minimum length of 8 characters.
  - At least one uppercase letter.
  - At least one lowercase letter.
  - At least one digit.
  - At least one special character (e.g., !, @, #, $, etc.).
- Provides clear feedback on password strength.
- Lists specific requirements for strong passwords if the input is weak.
- Uses regular expressions (`re` module) for pattern matching.
- Simple command-line interface for user interaction.

## Requirements
- **Python**: Version 3.x
- **Standard Library**: The script uses the `re` module, which is included with Python.
- No external libraries are required.

## Installation
1. Ensure Python 3.x is installed on your system.
2. Save the script as `password_strength_checker.py` in a directory of your choice.
3. No additional dependencies are needed, as the script uses Python's standard `re` module.

## Code
```python
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
```

## How It Works
1. **Main Function**:
   - Displays a header ("Password Strength Checker").
   - Prompts the user to input a password using `input()`.
   - Calls the `check_password_strength` function to evaluate the password.
   - Prints feedback based on the evaluation result.

2. **Password Strength Checking**:
   - The `check_password_strength` function evaluates the password against five criteria:
     - **Length**: Checks if the password is at least 8 characters long using `len(password)`.
     - **Uppercase Letters**: Uses `re.search(r'[A-Z]', password)` to check for at least one uppercase letter.
     - **Lowercase Letters**: Uses `re.search(r'[a-z]', password)` to check for at least one lowercase letter.
     - **Digits**: Uses `re.search(r'[0-9]', password)` to check for at least one digit.
     - **Special Characters**: Uses `re.search(r'[!@#$%^&*(),.?":{}|<>]', password)` to check for at least one special character from a predefined set.
   - Returns a tuple: `(is_strong, message)`, where `is_strong` is a boolean indicating if the password meets all criteria, and `message` is a string explaining the result.

3. **Output**:
   - If the password is strong, it prints a success message (e.g., "Success: Password is strong").
   - If the password is weak, it prints the specific reason (e.g., "Weak password: Password must contain at least one digit") and lists all requirements for a strong password.

## Usage
1. Save the script as `password_strength_checker.py`.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script using:
   ```bash
   python password_strength_checker.py
   ```
4. Enter a password when prompted.
5. The script will display whether the password is strong or weak, along with appropriate feedback.

## Example Output
### Strong Password
```
Password Strength Checker
------------------------
Enter a password to check: Password123!

Success: Password is strong
```

### Weak Password
```
Password Strength Checker
------------------------
Enter a password to check: pass

Weak password: Password must be at least 8 characters long
A strong password should:
- Be at least 8 characters long
- Contain both uppercase and lowercase letters
- Include at least one digit
- Include at least one special character (e.g., !, @, #, $, %
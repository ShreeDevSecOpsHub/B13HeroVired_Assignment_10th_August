# Password Strength Checker Documentation

Overview

The Password Strength Checker is a Python script designed to evaluate the strength of a password based on specific security criteria. This tool is useful in DevOps environments to enforce strong password policies and enhance security.

Purpose

The script checks if a password meets the following criteria:





Minimum length of 8 characters.



Contains at least one uppercase letter.



Contains at least one lowercase letter.



Contains at least one digit (0-9).



Contains at least one special character (e.g., !, @, #, $, %, etc.).

File





Password_Strength_checker.py: The main Python script that implements the password strength checking functionality.

Requirements





Python 3.x



Standard library module: re (for regular expressions)

Functionality

Main Components





check_password_strength(password)





Input: A string representing the password to be checked.



Output: A tuple containing:





A boolean indicating whether the password meets all criteria (True for strong, False for weak).



A message explaining the result (e.g., "Password is strong" or a specific reason why the password is weak).



Criteria Checked:





Length ≥ 8 characters.



Contains at least one uppercase letter ([A-Z]).



Contains at least one lowercase letter ([a-z]).



Contains at least one digit ([0-9]).



Contains at least one special character from the set [!@#$%^&*(),.?":{}|<>].



Implementation: Uses regular expressions (re module) to check for the presence of required character types.



main()





Prompts the user to input a password.



Calls check_password_strength to evaluate the password.



Provides feedback to the user based on the evaluation:





If the password is strong, displays a success message.



If the password is weak, displays the specific reason and lists all criteria for a strong password.
<img width="1468" height="508" alt="image" src="https://github.com/user-attachments/assets/ebf9b374-0775-47a5-a1cf-4a4f9fab3f02" />


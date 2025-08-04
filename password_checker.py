print(
    """
    Welcome to PASSWORD CHECKER program

    Instructions for being a VALID password:
    1. Password should start and end with alphabets only.
    2. Password must contain digits.
    3. Spaces are not allowed in password.
    4. Special characters are allowed.
    5. Length of password must be greater than or equal to 6.
"""
)
password = input("Enter a password to check: ")

def contain_digits(password: str) -> bool:
    """
    Function to check if password contains digit or not .
    """
    for char in password:
        if char.isdigit():
            return True
    return False

def contain_special(password: str) -> bool:
    """
    Function to check for other characters except alphabets and digits.
    """
    for char in password:
        if not (char.isalpha() or char.isdigit()):
            return True
    return False

def validity_checker(password: str) -> bool:
    if len(password) < 6:
        return False
    if not (password[0].isalpha() or password[-1].isalpha()):
        return False
    if password.find(" ") != -1:
        return False
    if not contain_digits(password):
        return False
    return True

def strength(password: str) -> str:
    if len(password) > 14:
        if contain_special(password):
            return "Strong"
        return "Medium"
    if len(password) > 10 and contain_special(password):
        return "Medium"
    return "Weak"

if validity_checker(password):
    print("VALID PASSWORD!", strength(password))
else:
    print("INVALID PASSWORD!")

# Use caesar cipher file and convert them into secured ones.
# Save these passwords in a json file/db
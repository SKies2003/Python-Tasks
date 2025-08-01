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
    for i in range(1, len(password)-1):
        if password[i].isdigit():
            return True
    return False

def validity_checker(password: str) -> bool:
    if len(password) < 6:
        return False
    for i in range(len(password)):
        if i == 0 or i == len(password)-1:
            if not password[i].isalpha():
                return False
        else:
            if ord(password[i]) == 32:
                    return False
    if not contain_digits(password):
        return False
    return True

if validity_checker(password):
    print("VALID PASSWORD!")
else:
    print("INVALID PASSWORD!")
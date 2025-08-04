from password_checker import instructions, check_password
from caesar_cipher import shift_text

if __name__ == "__main__":
    print(instructions())
    user = input("Enter a password: ")
    print(check_password(user))
    if check_password(user).startswith("VALID"):
        encrypted_password = shift_text("e", user)
        print(encrypted_password)
# The Caesar cipher is a simple encryption technique that was used by Julius Caesar to send secret messages to his allies.

def shift_text(operation: str, text: str) -> str:
    """ Finds shifted text from given text

    Args:
        Operation: Operation to perform selected by user (e: encrypt/d: decrypt)
        text: An English message given by user.
    
    Returns:
        new_text: An English message on which operation is performed
    """
    new_text = ""
    if operation == 'e':
        shift = 3
    else:
        shift = -3
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_text += chr((ord(char)- base + shift) % 26 + base)
        else:
            new_text += char
    return new_text

def user_choice():
    """
    Function to ask for user choices whther to perform encryption, decryption or exit the program.
    """
    while True:
        user = input(("Enter e to encrypt, d to decrypt, or any other key to exit: "))
        if user.lower() == 'e':
            text = input("Enter the message you want to encrypt: ")
            print(shift_text(user, text), end="\n\n")
        elif user.lower() == 'd':
            operation = "decrypt"
            text = input("Enter the message you want to decrypt: ")
            print(shift_text(user, text), end="\n\n")
        else:
            print("Program Exited.")
            break


if __name__ == "__main__":
    print("\nWelcome to CAESAR CIPHER ENCRYPTION DECRYPTION program\n")
    user_choice()
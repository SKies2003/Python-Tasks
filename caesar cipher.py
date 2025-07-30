# The Caesar cipher is a simple encryption technique that was used by Julius Caesar to send secret messages to his allies.

def encrypt(plain_text: str) -> str:
    """Finds cipher text from plain text.

    Args:
        plain_text (str): An English message in human understandable language.
    Returns:
        cipher_text (str): An English message in human non-understandable language.
    """
    cipher_text = ""
    for char in plain_text:
        cipher_text += chr(ord(char) + 3)
    return cipher_text

def decrypt(cipher_text: str) -> str:
    """Finds plain text from cipher text.

    Args:
        cipher_text (str): An English message in human non-understandable language.
    Returns:
        plain_text (str): An English message in human understandable language.
    """
    plain_text = ""
    for char in cipher_text:
        plain_text += chr(ord(char) - 3)
    return plain_text

while True:
    user = input(("Enter e to encrypt message\nEnter d to decrypt message\nAnyother key to exit: "))
    if user.lower() == 'e':
        plain_text = input("Enter the message you want to encrypt: ")
        print(encrypt(plain_text), end="\n\n")
    elif user.lower() == 'd':
        cipher_text = input("Enter the message you want to decrypt: ")
        print(decrypt(cipher_text), end="\n\n")
    else:
        print("Exit")
        break
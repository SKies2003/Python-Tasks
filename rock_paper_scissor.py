import random

options = ["rock", "paper", "scissor"]


def user_choice():
    user = input(
        """
    For choosing rock press: R or r or 1 or rock
    For choosing paper press: P or p or 2 or paper
    For choosing scissor press: S or s or 3
    To Exit press any other key or input
    """
    )

    if user.isalpha():
        if user.lower() == "r" or user.lower() == "rock":
            return "rock"
        elif user.lower() == "p" or user.lower() == "paper":
            return "paper"
        elif user.lower() == "s" or user.lower() == "scissor":
            return "scissor"
        else:
            print("Exit!")
            return None
    elif user.isdigit():
        if user == "1":
            return "rock"
        elif user == "2":
            return "paper"
        elif user == "3":
            return "scissor"
        else:
            print("Exit!")
            return None
    else:
        print("Exit!")
        return None


def game():
    while True:
        computer = random.choice(options)
        you = user_choice()

        if you is None:
            break

        print(f"You chose: {you}")
        print(f"Computer chose: {computer}")

        if you == computer:
            print("It's a draw!")
        elif (
            (you == "rock" and computer == "scissor")
            or (you == "paper" and computer == "rock")
            or (you == "scissor" and computer == "paper")
        ):
            print("You win!")
        else:
            print("Computer wins!")


if __name__ == "__main__":
    game()

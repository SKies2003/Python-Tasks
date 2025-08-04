# Problem Statement:
# Create a game where the computer randomly selects a number between 1 and 100. The user tries to guess the number, and the program provides feedback: "Too high", "Too low", or "Correct". Keep count of how many guesses the user takes.

# Skills Used:
# Inputs/Outputs, Conditional statements, Loops, Functions, Random module.


import random

computer = random.randint(1, 100)
count = 0

while True:
    guess = int(input("Make a guess between 1 and 100: "))
    count += 1
    if guess == computer:
        print("Correct")
        print(f"You solved the game in {count} tries")
        break
    elif guess > computer:
        print("Too high")
    else:
        print("Too low")
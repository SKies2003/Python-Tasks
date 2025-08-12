from random import choice

words = ["Python", "Programming", "Developers", "Computers", "Servers", "Database", "Github", "Stackoverflow", "Terminal", "Mathematics", "Google", "Youtube", "GeeksforGeeks"]

word = choice(words)
print(f"{len(word)} characters")
word_lst = list(set(i.lower() for i in word))

guess = 0
lst = []

while True:
    char = input("Make a guess: ").lower()
    if char in word.lower():
        lst.append(char)
    guess += 1
    for i in range(len(word)):
        if word[i].lower() in lst:
            print(word[i], end=" ")
        else:
            print("_", end=" ")
    print()
    if len(word_lst) == len(lst):
        print(f"You took total {guess} guesses.")
        break
import os, random
os.system("clear") #clears the screen

green = "\u001b[42m" #The letter is in the word and in the right place
yellow = "\u001b[43m" #The letter is in the word but wrong place
reset = "\u001b[0m" #reset the color

print("WORDLE")

correct = random.choice(["shake", "share", "panic", "amuse", "shape"]).upper() #Picks the correct word randomly from these choices

for _ in range(6): #we get 6 chances
    guess = input("Please guess. > ").upper() #used to insert input

    #check first letter
    for i in range(0, 5):
        if guess[i] == correct[i]:
            print(f"{green}{guess[i]}{reset}", end="")
        elif guess[i] in correct:
            print(f"{yellow}{guess[i]}{reset}", end="")
        else:
            print(guess[i], end="")
    print()

    #check if guess is correct
    if guess == correct:
        print("You win!")
        exit()
print("You lose!")
print(f"The correct word is {correct}.")
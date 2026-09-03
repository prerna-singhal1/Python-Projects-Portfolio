# Rock, Paper, Scissor Game

import random

choices = ("rock", "paper", "scissor")
running = True


while running:
    computer = random.choice(choices)
    human = None

    while human not in choices:
        human = input("What would you like to choose? Rock, Paper or Scissor? ").lower()
        if human not in choices:
            print("Invalid input!")
            print("TRY AGAIN!")

    print(f"Computer chose: {computer}")
    print(f"You chose: {human}")

    if computer == human:
        print("It is a TIE")
    elif computer == "rock" and human == "scissor":
        print("You LOSE!")
    elif computer == "paper" and human == "rock":
        print("You LOSE!")
    elif computer == "scissor" and human == "paper":
        print("You LOSE!")
    else:
        print("You WIN!")

    play_again = input("Would you like to play again(y for yes and n for no): ").lower()
    if play_again == "y":
        continue
    if not play_again == "y" or "n":
        print("Sorry, You entered a wrong input.")
        running = False
    else:
        running = False

print("Thanks for Playing!")

        
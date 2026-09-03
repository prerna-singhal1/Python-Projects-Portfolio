#Python Number Guessing Game

import random

high = 100
low = 1
count = 0

print("Welcome to the Python Number Guessing Game!")

print(f"Select a number between {low} and {high}")

number = random.randint(low, high)

while True:
    guess = input("Enter your Guess: ")
    count += 1
    if guess.isdigit():
        guess = int(guess)
        if not low < guess < high:
            print("You entered a number which was out of range." \
                  f"Try Again! Please select a number between {low} and {high}.")
        elif guess < number:
            print("Too Low, Try Again!")
        elif guess > number: 
            print("Too High, Try Again!")           
        elif guess == number:
            print(f"CORRECT! The number was {number}.")
            break
    else:
        print("Invalid Guess!" \
        f"Try Again! Please select a number between {low} and {high}.")


print(f"Number of guesses: {count}")
    




#Python Slot Machine Program

import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    # results = []
    # for symbol in range(3):
    #     results.append(random.choice(symbols))
    # return results
    return [random.choice(symbols) for symbol in range(3)]

def print_row(row):
    print("************************")
    print(" | ".join(row))
    print("************************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            print("CHERRY LOTTERY!")
            return bet * 3
        elif row[0] == "🍉":
            print("WATERMELON LOTTERY!")
            return bet * 4
        elif row[0] == "🍋":
            print("LEMON LOTTERY!")
            return bet * 2
        elif row[0] == "🔔":
            print("BELL LOTTERY!")
            return bet * 5
        elif row[0] == "⭐":
            print("STAR LOTTERY!")
            return bet * 10
    return 0



def main():
    balance = 100

    print("************************")
    print("Welcome to Python Slots!")
    print("Symbols:🍒 🍉 🍋 🔔 ⭐")
    print("************************")


    while balance>0:
        
        print("************************")
        print(f"Current Balance: ${balance:.2f}")
        print("************************")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("************************")
            print("You have entered an invalid bet amount.")
            print("Please enter a valid amount.")
            continue

        bet = int(bet)

        if bet > balance:
            print("************************")
            print("You do not have sufficient balance.")
            print("Please enter a valid amount.")
            continue
        if bet <= 0:
            print("************************")
            print("Bet must be greater tham zero.")
            print("Please enter a valid amount.")
            continue
        
        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}!")
        else:
            print(f"Sorry, You lost!\nTry Again!:)")

        balance += payout

        play_again = input("Do you want to spin again?(Y/N): ").upper()
        if play_again != "Y":
            break
    
    print("************************************************")
    print(f"Game Over!\nYour current balance is : ${balance}")
    print("************************************************")


if __name__ == '__main__':
    main()
#Python Banking Program

def show_balance(balance):
    print("***********************************")
    print(f"Your balance is ${balance:.2f}")
    print("***********************************")

def deposit():
    print("***********************************")
    amount = float(input("Enter an amount to be depositied: "))
    print("***********************************")

    if amount < 0:
        print("***********************************")
        print("You have entered an invalid amount!")
        print("***********************************")
        return 0
    else:
        return amount

def withdraw(balance):
    print("***********************************")
    out = float(input("Enter an amount to be withdrawn: "))
    print("***********************************")

    if out > balance:
        print("***********************************")
        print("Your account does not have sufficient money.")
        print("***********************************")
        return 0
    elif out < 0:
        print("***********************************")
        print("You have entered an invalid withdrawal amount!")
        print("***********************************")
        return 0
    else:
        return out
    
def main():
    balance = 0
    is_running = True
    while is_running:
        print("***********************************")
        print("Banking Program")
        print("***********************************")

        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("***********************************")

        choice = input("Enter your choice(1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("***********************************")
            print("That is not a Valid choice.")
            print("***********************************")
    
    print("***********************************")
    print("Thank you! Have a nice Day :)")
    print("***********************************")

        

if __name__ == '__main__':
    main()


#Concession Stand Program

# dictionary {Key : Value}

concessions = { "popcorn" : 6.40, 
               "burger": 8.70, 
               "pretzel" : 2.50, 
               "candy" : 3.60, 
               "coldrink" : 4.00, 
               "bottled Water" : 2.50,
               "pizza" : 10.99,
               "fries" : 5.85 }

cart = []
total = 0

print("       This is the Menu Card      ")

print("----------------------------------")

items = concessions.items()
for key, value in items:
    print(f"{key:10} : ${value: .2f}")

print("-----------------------------------")

while True:
    food = input("Which items would you like to buy from the Menu Card (q to quit): ").lower()
    if food == "q":
        break
    elif concessions.get(food) == None: 
        print("You have entered an item which is not present in the menu." \
         "Please enter a different item.")
    elif not concessions.get(food) == None:
        cart.append(food)
    
print("------------ YOUR ORDER ------------")

for food in cart:
    total += concessions.get(food)
    print(food, end = " ")

print()

print(f"Your total is: ${total: .2f}")





# Shopping Cart Program

foods = []
prices = []
total = 0

while True:
    food = input("Which item would you like to add in your basket? (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of the {food}: $ "))
        foods.append(food)
        prices.append(price)
    
print("****Your Cart****")
for food in foods:
    print(food)

print("****Your Bill****")
for price in prices:
    total += price
    print(price)

print(f"The total bill amount for you shopping cart is: ${total}.")


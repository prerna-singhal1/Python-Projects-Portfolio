number = int(input("Enter a number between 1 to 10. "))

while number<1 or number>10:
    print(f"Your entered number is invalid.")
    number = int(input("Enter a number between 1 to 10. "))

print(f"Your chosen number is {number}")






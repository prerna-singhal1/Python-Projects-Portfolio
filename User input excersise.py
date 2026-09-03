username = input("Enter your username. ")

# if username.find(" ") > 0:
#     print("Sorry, invalid username input.")
if len(username)>12:
    print("Sorry, invalid username input.")
elif username.isalpha() == False:
    print("Sorry, invalid username input.")
else:
    print("Your username input is valid.")
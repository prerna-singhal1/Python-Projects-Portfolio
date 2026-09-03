#Python Compund Interest Calculator

# A = P(1+ r/100)^t

P = float(input("Enter your initial balance: "))
while P < 0:
    print("Entred invalid initial balance.")
    P = float(input("Enter your initial balance: "))


r = float(input("What is the rate of interest? "))
while r < 0:
    print("Entred invalid rate of interest.")
    r = float(input("What is the rate of interest? "))


t = float(input("What is the number of years you want the interest to act on? "))
while t < 0:
    print("Entred invalid number of years.")
    t = float(input("What is the number of years you want the interest to act on? "))


A = P * ((1 + (r/100))**t)

print(f"Your desired final amount after compound interest is: {round(A, 2)}")
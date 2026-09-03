Rows = int(input("Number of Rows the rectangle will have: "))
Columns = int(input("Number of Columns the rectangle will have: "))
symbol = input("Enter a symbol to choose: ")

for x in range(Rows):
    for y in range(Columns):
        print(symbol, end = "")
    print()


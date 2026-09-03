import csv

file_path = "C:/Users/PRERNA/OneDrive/Desktop/outpout.csv"
        
try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)

except FileNotFoundError:
    print("FILE WASN'T FOUND!!")
import csv

employees = [["Name", "Age", "Job"],
             ["Prerna", 20, "CTO"],
             ["Aaditi", 30, "CEO"],
             ["Krishna", 40, "CTO"]]

file_path = "C:/Users/PRERNA/OneDrive/Desktop/output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file {file_path} was created.")

except FileExistsError:
    print("FILE ALREADY EXISTS!!")

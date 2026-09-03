# Python Quiz game

questions = ("Q1) What is the hardest natural substance on Earth?" , 
            "Q2) Who was the first person to discover Gravity?",
            "Q3) Who is India's Prime Minister?",
            "Q4) What is a room with no doors called?",
            "Q5) What is the approx. radius of Earth?")

options = (("A: Diamond", "B: Graphite", "C: Bromine", "D: Glass"),
           ("A: Einstein", "B: Archemedie", "C: Newton", "D: Bohr"), 
           ("A: Narendra Modi", "B: Rahul Gandhi", "C: Indira Gandhi", "D: Akhilesh Yadav"), 
           ("A: Window", "B: Bathroom", "C: Mushroom", "D: Home"), 
           ("A: 6000 km", "B: 3200 km", "C: 3000 km", "D: 6400 km"))

question_number = 0

guesses = []

score = 0

answers = ("A", "C", "A", "C", "D")

print("QUIZ GAME!")

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[question_number]:
        print(option)
    
    guess = input("Enter A, B, C or D: "). upper()
    while guess not in ("A", "B", "C", "D"):
        print("You entered an invalid Guess. TRY AGAIN!")
        guess = input("Enter A, B, C or D: "). upper()

    guesses.append(guess)
    if guess == answers[question_number]:
            score += 1
            print("CORRECT!")
    else:
            print("INCORRECT!")
            print(f"The correct answer is {answers[question_number]}")

    question_number += 1

print("-----------------------------------------------")

print("Congratulations! You have sucessfully completed the Quiz.")

print("-----------------------------------------------")

print("                   RESULTS                     ")

print("-----------------------------------------------")

print("Answers: ", end = "")
for answer in answers:
    print(answer, end = " ")
print()

print("Guesses: ", end = "")
for guess in guesses:
    print(guess, end = " ")
print()

print(f"You got {score} questions right out of {len(questions)}.")

final_score = int((score/len(questions)) * 100)

print(f"Your score is {final_score}%.")


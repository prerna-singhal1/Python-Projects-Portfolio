#Hangman Game
import random

words = [
    "cuisine", "ingredient", "delicacy", "beverage", "appetizer", "dessert",
    "nutrition", "recipe", "marinade", "savory", "spicy", "organic",
    "processed", "portion", "platter", "dairy", "cereal", "grains",
    "legumes", "condiments", "fermented", "refreshment", "bakery",
    "pastry", "sauce", "protein", "carbohydrate", "vitamin", "mineral", "snack",

    "mammal", "reptile", "amphibian", "predator", "herbivore", "carnivore",
    "omnivore", "habitat", "species", "domestic", "wild", "nocturnal",
    "endangered", "migration", "instinct", "vertebrate", "invertebrate",
    "aquatic", "terrestrial", "feline", "canine", "hooves", "claws",
    "feathers", "fur", "scales", "prey", "ecosystem", "camouflage", "survival",

    "appliance", "furniture", "device", "equipment", "gadget", "tool",
    "container", "material", "resource", "object", "structure", "surface",
    "mechanism", "engine", "battery", "cable", "switch", "display", "storage",
    "packaging", "instrument", "vehicle", "accessory", "stationery",
    "document", "currency", "balance", "weight", "measurement", "quantity",
    "quality", "function", "purpose", "design", "pattern", "texture",
    "shape", "volume", "capacity", "durability"
]


game = {0: ("     ",
            "     ",
            "     "),
        1: ("  o  ",
            "     ",
            "     "),
        2: ("  o  ",
            "  |  ",
            "     "),
        3: ("  o  ",
            " /|  ",
            "     "),
        4: ("  o  ",
            " /|\\",
            "     "),
        5: ("  o  ",
            " /|\\",
            "  |  "),
        6: ("  o  ",
            " /|\\",
            " /|  "),
        7: ("  o  ",
            " /|\\",
            " /|\\"),
}

def incorrect(wrong_guesses):
    print("***********************")
    for line in game[wrong_guesses]:
        print(line)
    print("***********************")

def help(hint):
    print(" ".join(hint))
    

def correct(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        incorrect(wrong_guesses)
        help(hint)

        guess = input("Enter the letter to guess: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid Guess...Enter a correct guess!")
            continue
        
        if guess in guessed_letters:
            print(f"You have already guessed the letter: {guess}\nTry another letter.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            incorrect(wrong_guesses)
            correct(answer)
            print("Congratulations! YOU WIN!🌟💫")
            is_running = False

        elif wrong_guesses >= len(game) - 1:
            incorrect(wrong_guesses)
            correct(answer)
            print("Better luck next time...YOU LOOSE!🥲")
            is_running = False


        


if __name__ == "__main__":
    main()



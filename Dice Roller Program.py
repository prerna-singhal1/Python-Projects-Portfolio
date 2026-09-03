# Python Dice Roller Program

import random

# ● ┌ ─ ┐ │ └ ┘

dice = {1:(
           "┌─────────┐",
           "│         │",
           "│    ●    │",
           "│         │",
           "└─────────┘",
        ),
        2:(
           "┌─────────┐",
           "│  ●      │",
           "│         │",
           "│      ●  │",
           "└─────────┘",
        ),
        3:(
           "┌─────────┐",
           "│ ●       │",
           "│    ●    │",
           "│       ● │",
           "└─────────┘",
        ), 
        4:(
           "┌─────────┐",
           "│ ●     ● │",
           "│         │",
           "│ ●     ● │",
           "└─────────┘",
        ),
        5:(
           "┌─────────┐",
           "│ ●     ● │",
           "│    ●    │",
           "│ ●     ● │",
           "└─────────┘",
        ),
        6:(
           "┌─────────┐",
           "│  ●   ●  │",
           "│  ●   ●  │",
           "│  ●   ●  │",
           "└─────────┘",
        )
    }

dices = []
total = 0

user = int(input("How many dice would you like to have: "))

for die in range(user):
    dices.append(random.randint(1, 6))

# for die in range(user):
#     for figure in dice.get(dices[die]):
#         print(figure)

for line in range(5):
    for die in dices:
        print(dice.get(die)[line], end = "")
    print()

for die in dices:
    total += die

print(f"The total is: {total}")
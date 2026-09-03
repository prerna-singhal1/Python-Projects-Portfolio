# 2D Keypad

telephone_dial_pad = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ('*', 0, '#'))
for number in telephone_dial_pad:
    for row in number:
        print(row, end=" ")
    print()

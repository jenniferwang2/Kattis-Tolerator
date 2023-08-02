position = 1
for move in [*input()]:
    if move == "A": 
        if position == 2:
            position = 1
        elif position == 1:
            position = 2
    elif move == "B":
        if position == 3:
            position = 2
        elif position == 2:
            position = 3
    elif move == "C":
        if position == 3:
            position = 1
        elif position == 1:
            position = 3
print(position)
    
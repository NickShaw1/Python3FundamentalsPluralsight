import random

def roll_dice():
    dice_total = random.randint(1,3) + random.randint(1,3)
    return dice_total

def dicegame():
    input1 = input("Enter Player 1's name:\n")
    input2 = input("Enter Player 2's name:\n")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(input1, "rolled ", roll1)
    print(input2, "rolled", roll2)

    if roll1 > roll2:
        print(input1, "wins with a roll of", roll1)
    elif roll2 > roll1:
        print(input2, "wins with a roll of", roll2)
    else:
        print("Tie!")

dicegame()
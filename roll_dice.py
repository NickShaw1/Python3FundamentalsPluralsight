import random
roll = random.randint (1,6)
guess = int(input("Guess the dice roll:\n"))
if guess == roll:
    print("Correct, the computer rolled " + str(roll))
else:
    print("Incorrect, the computer rolled " + str(roll))
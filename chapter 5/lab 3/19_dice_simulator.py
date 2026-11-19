import random

while True:

    input("Press Enter to roll dice")

    number = random.randint(1, 6)

    print("Dice number:", number)

    choice = input("Roll again? (y/n): ")

    if choice.lower() != "y":
        break
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        try:
            guess = int(input(f'Guess a number between 1 and {x}: '))
        except ValueError:
            print("That's not an int!")
            exit()
        if guess < random_number:
            print('Guess again. Too low.')
        elif guess > random_number:
            print('Guess again. Too high.')

    print(f'You have guessed the number {random_number} correctly.')

try:
    range = int(input("Please enter range: "))
    guess(range)
except ValueError:
    print("That's not an int!")

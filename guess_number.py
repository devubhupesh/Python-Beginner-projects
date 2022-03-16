import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('sorry, guess again, too low')
        elif guess > random_number:
            print('sorry, try again, too high')
    print('yay!! congrats u have guessed right')   
guess(10)
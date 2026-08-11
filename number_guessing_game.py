import random

number = random.randint(1, 100)

guess = int(input("Guess the number: "))

while True:
    guess = int(input("Guess the number: "))

    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print("Correct! You guessed the number!")
        break

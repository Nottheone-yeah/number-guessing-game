import random

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print(f"Correct! You got it in {attempts} attempts!")
        break
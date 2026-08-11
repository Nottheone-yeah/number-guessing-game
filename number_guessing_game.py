import random

number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Guess the number: "))
    except ValueError:
        print("Please enter a number!")
        continue
    
    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100!")
        continue

    attempts += 1

    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print(f"Correct! You got it in {attempts} attempts!")
        break
import random

print("Choose your difficulty:")
print("1. Easy   (1-50)")
print("2. Medium (1-100)")
print("3. Hard   (1-500)")

while True:
    difficulty = input("Enter your choice: ")

    if difficulty in ["1", "2", "3"]:
        break

    print("Invalid choice! Please enter 1, 2, or 3.")

if difficulty == "1":
    maximum = 50
elif difficulty == "2":
    maximum = 100
else:
    maximum = 500

number = random.randint(1, maximum)
attempts = 0

while True:
    try:
        guess = int(input("Guess the number: "))
    except ValueError:
        print("Please enter a number!")
        continue

    if guess < 1 or guess > maximum:
        print(f"Please enter a number between 1 and {maximum}!")
        continue

    attempts += 1

    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print(f"Correct! You got it in {attempts} attempts!")
        break
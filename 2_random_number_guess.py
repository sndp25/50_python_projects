from random import randint as rn

def guess_the_number():
    alpha = rn(0, 9)
    attempts = 0
    max_attempts = 3  # Set a limit for the number of attempts

    print("Guess the number between 0 and 9")

    while attempts < max_attempts:
        try:
            beta = int(input("> "))
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 9.")
            continue

        if beta < 0 or beta > 9:
            print("Please enter a number between 0 and 9.")
            continue

        attempts += 1

        if beta == alpha:
            print("You are Correct!")
            break
        elif beta < alpha:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        if attempts == max_attempts:
            print(f"Better luck next time! The number was {alpha}.")
            break

guess_the_number()

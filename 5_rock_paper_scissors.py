from random import choice as ch

user_score = 0
comp_score = 0
tries = 0

print("Winner will be the best of three matches")

while tries < 3:
    comp = ch(["R", "P", "S"])

    # Input with proper handling
    try:
        choice = int(input(f"(1)Rock (2)Paper (3)Scissors (4)Exit ({tries + 1}, Round!) >> "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue

    if choice == 4:
        print("Exiting the game.")
        break

    if choice == comp:
        print(f"*Draw* [user] -> {['Rock', 'Paper', 'Scissors'][choice - 1]} v/s {['Rock', 'Paper', 'Scissors'][['R', 'P', 'S'].index(comp)]} <- [comp]")

    elif choice == 1:
        print("[user] -> Rock v/s ", end="")
        if comp == "P":
            print("Paper <- [comp]")
            comp_score += 1
        else:
            print("Scissors <- [comp]")
            user_score += 1
    elif choice == 2:
        print("[user] -> Paper v/s ", end="")
        if comp == "R":
            print("Rock <- [comp]")
            user_score += 1
        else:
            print("Scissors <- [comp]")
            comp_score += 1
    elif choice == 3:
        print("[user] -> Scissors v/s ", end="")
        if comp == "R":
            print("Rock <- [comp]")
            comp_score += 1
        else:
            print("Paper <- [comp]")
            user_score += 1
    else:
        print("Invalid choice, please choose between 1, 2, 3, or 4.")
        continue

    tries += 1
    print(f"User: {user_score} \t Comp: {comp_score}")

# Final Result
if user_score > comp_score:
    print("User Won!")
elif user_score < comp_score:
    print("User Lost!")
else:
    print("It's a Draw!")

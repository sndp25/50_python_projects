def perform_calculation():
    print("Please choose the action you want to perform")
    print("(1) Addition")
    print("(2) Subtraction")
    print("(3) Multiplication")
    print("(4) Division")

    try:
        choice = int(input("> "))
    except ValueError:
        print("Invalid choice! Please enter a number between 1 and 4.")
        return

    try:
        num_1 = float(input("Enter First Number: "))
        num_2 = float(input("Enter Second Number: "))
    except ValueError:
        print("Invalid number! Please enter valid numeric values.")
        return

    print()

    if choice == 1:
        print(f"Result: {num_1 + num_2}")
    elif choice == 2:
        print(f"Result: {num_1 - num_2}")
    elif choice == 3:
        print(f"Result: {num_1 * num_2}")
    elif choice == 4:
        if num_2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            print(f"Result: {num_1 / num_2}")
    else:
        print("Invalid choice! Please choose a valid operation.")

def calculator():
    while True:
        perform_calculation()
        cont = input("Do you want to perform another calculation? (yes/no): ").lower()
        if cont != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

# Run the calculator
calculator()

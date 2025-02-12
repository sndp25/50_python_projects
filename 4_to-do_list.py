to_do = []

print("** Welcome To TO-DO List **")

while True:
    print("\n(1) Add a Task")
    print("(2) Remove a Task")
    print("(3) View Tasks")
    print("(4) Exit")
    
    try:
        Choice = int(input("Select an option: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 4.")
        continue

    if Choice == 1:
        task = input("Enter the task to add: ")
        to_do.append(task)
        print(f"Task '{task}' added.")

    elif Choice == 2:
        if not to_do:
            print("No tasks to remove!")
        else:
            try:
                index = int(input("Enter the index of the task to delete: ")) - 1
                if index < 0 or index >= len(to_do):
                    print("Invalid index! Please enter a valid task index.")
                else:
                    removed_task = to_do.pop(index)
                    print(f"Task '{removed_task}' removed.")
            except ValueError:
                print("Invalid input! Please enter a valid number for the index.")
            except IndexError:
                print("Index out of range. Please try again.")

    elif Choice == 3:
        if not to_do:
            print("Your to-do list is empty!")
        else:
            print("\n** Your Tasks **")
            for idx, task in enumerate(to_do, start=1):
                print(f"{idx}. {task}")

    elif Choice == 4:
        print("Exiting the To-Do List Manager. Goodbye!")
        break

    else:
        print("Invalid choice! Please select a valid option between 1 and 4.")

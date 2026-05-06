"""
To-Do List CLI Application
A simple command-line app to add, view, and delete tasks.
"""

def display_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")


def add_task(tasks):
    try:
        task = input("Enter a new task: ").strip()
        if task == "":
            raise ValueError("Task cannot be empty.")
        tasks.append(task)
        print(f"Task added: {task}")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print("Task successfully saved.")
    finally:
        print("Returning to menu...")


def view_tasks(tasks):
    try:
        if len(tasks) == 0:
            raise Exception("No tasks available.")
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    except Exception as e:
        print(f"Notice: {e}")
    finally:
        print("Returning to menu...")


def delete_task(tasks):
    try:
        if len(tasks) == 0:
            raise Exception("No tasks to delete.")

        view_tasks(tasks)
        choice = int(input("Enter the task number to delete: "))

        if choice < 1 or choice > len(tasks):
            raise IndexError("Task number does not exist.")

        removed = tasks.pop(choice - 1)
        print(f"Deleted task: {removed}")

    except ValueError:
        print("Error: Please enter a valid number.")
    except IndexError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Notice: {e}")
    else:
        print("Task successfully removed.")
    finally:
        print("Returning to menu...")


def main():
    tasks = []
    print("Welcome to the To-Do List App!")

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        try:
            if choice == "1":
                add_task(tasks)
            elif choice == "2":
                view_tasks(tasks)
            elif choice == "3":
                delete_task(tasks)
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                raise ValueError("Invalid menu option.")

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
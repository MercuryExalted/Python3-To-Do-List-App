def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def main():
    tasks = [] # Local database
    while True:
        show_menu()
        choice = input("Choose an option (1-4):")

        if choice == '1':
                view_tasks(tasks)
        elif choice == '2':
                add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

def view_tasks(tasks):
    if not tasks:
        print("\nYour list is empty")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    new_task = input("Enter the task: ")
    tasks.append(new_task)
    print("Task added!")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")

# Runs app
if __name__ == "__main__":
    main()
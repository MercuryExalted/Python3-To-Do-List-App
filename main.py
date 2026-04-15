def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def main()
    tasks = [] # Local database
    while True:
        show_menu()
        choice = input("Choose an option (1-4):")

        if choice == '1':
                view_tasks(tasks)
        elif choice == '2':
                add_task(tasks)
        elif choice == '3':
            remove_tasks(tasks)
        elif choice == '4'
            print("Goodbye!")
            break
        else
            print("Invalid choice, try again.")

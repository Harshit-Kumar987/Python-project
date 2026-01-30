tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        if not tasks:
            print("No tasks.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    elif choice == "3":
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")
        num = int(input("Enter task number: "))
        tasks.pop(num - 1)
        print("Task deleted.")

    elif choice == "4":
        print("Exiting.")
        break

    else:
        print("Invalid choice.")

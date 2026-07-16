from todo import Todo


def menu():
    print("\n========== TO-DO LIST MANAGEMENT ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Search Task")
    print("7. Filter Pending Tasks")
    print("8. Filter Completed Tasks")
    print("9. Exit")


def main():
    todo = Todo()

    while True:
        menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\n--- Add Task ---")
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date (YYYY-MM-DD): ")
            priority = input("Priority (High/Medium/Low): ")

            todo.add_task(title, description, due_date, priority)

        elif choice == "2":
            print("\n--- All Tasks ---")
            todo.view_tasks()

        elif choice == "3":
            print("\n--- Update Task ---")
            task_id = int(input("Task ID: "))
            title = input("New Title: ")
            description = input("New Description: ")
            due_date = input("New Due Date: ")
            priority = input("New Priority: ")

            todo.update_task(
                task_id,
                title,
                description,
                due_date,
                priority
            )

        elif choice == "4":
            print("\n--- Delete Task ---")
            task_id = int(input("Task ID: "))
            todo.delete_task(task_id)

        elif choice == "5":
            print("\n--- Mark Task as Completed ---")
            task_id = int(input("Task ID: "))
            todo.mark_complete(task_id)

        elif choice == "6":
            print("\n--- Search Task ---")
            keyword = input("Enter keyword: ")
            todo.search_task(keyword)

        elif choice == "7":
            print("\n--- Pending Tasks ---")
            todo.filter_status("Pending")

        elif choice == "8":
            print("\n--- Completed Tasks ---")
            todo.filter_status("Completed")

        elif choice == "9":
            todo.close()
            print("\nThank you for using the To-Do List Management System!")
            break

        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()

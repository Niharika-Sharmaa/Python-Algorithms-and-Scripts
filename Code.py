class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def complete_task(self):
        self.completed = True


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print("\nTask added successfully!")

    def view_tasks(self):
        if len(self.tasks) == 0:
            print("\nNo tasks in the list.")
            return

        print("\n----- MY TO-DO LIST -----")

        for i, task in enumerate(self.tasks, 1):
            if task.completed:
                status = "Completed"
            else:
                status = "Pending"

            print(f"{i}. {task.description} - {status}")

    def mark_completed(self, task_number):
        if task_number >= 1 and task_number <= len(self.tasks):
            self.tasks[task_number - 1].complete_task()
            print("\nTask marked as completed!")
        else:
            print("\nInvalid task number.")


todo = TodoList()

while True:
    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        description = input("Enter task description: ")

        if description.strip() == "":
            print("\nTask description cannot be empty.")
        else:
            todo.add_task(description)

    elif choice == "2":
        todo.view_tasks()

    elif choice == "3":
        todo.view_tasks()

        if len(todo.tasks) > 0:
            try:
                task_number = int(input("\nEnter the task number: "))
                todo.mark_completed(task_number)
            except ValueError:
                print("\nPlease enter a valid number.")

    elif choice == "4":
        print("\nExiting To-Do List. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please select 1, 2, 3, or 4.")
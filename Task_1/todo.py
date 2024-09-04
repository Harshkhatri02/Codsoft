# A simple command-line To-Do List application in Python

# Define the list to store tasks
todo_list = []

def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Exit")

def view_todo_list():
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("\nEnter the task to add: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

def update_task():
    view_todo_list()
    if todo_list:
        task_number = int(input("\nEnter the number of the task to update: "))
        if 1 <= task_number <= len(todo_list):
            updated_task = input("Enter the updated task: ")
            todo_list[task_number - 1] = updated_task
            print(f"Task {task_number} updated to '{updated_task}'.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks available to update.")

def remove_task():
    view_todo_list()
    if todo_list:
        task_number = int(input("\nEnter the number of the task to remove: "))
        if 1 <= task_number <= len(todo_list):
            removed_task = todo_list.pop(task_number - 1)
            print(f"Task '{removed_task}' removed from the list.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks available to remove.")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        if choice == '1':
            view_todo_list()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            remove_task()
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

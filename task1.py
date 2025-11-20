# Simple To-Do List Application

# Dictionary to store tasks with status
todo_list = {}

def show_menu():
    print("\n========== 📝 TO-DO LIST MENU ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Exit")
    print("========================================")

def add_task():
    task_name = input("Enter task name: ")
    todo_list[task_name] = "Pending"
    print(f"✅ Task '{task_name}' added successfully!")

def view_tasks():
    if not todo_list:
        print("📭 No tasks in your to-do list.")
    else:
        print("\n📋 Your To-Do List:")
        for i, (task, status) in enumerate(todo_list.items(), start=1):
            print(f"{i}. {task} --> {status}")

def update_task():
    old_task = input("Enter the task name you want to update: ")
    if old_task in todo_list:
        new_task = input("Enter new task name: ")
        todo_list[new_task] = todo_list.pop(old_task)
        print(f"✏️ Task '{old_task}' updated to '{new_task}'!")
    else:
        print("❌ Task not found!")

def mark_completed():
    task = input("Enter the task name to mark as completed: ")
    if task in todo_list:
        todo_list[task] = "Completed"
        print(f"🏁 Task '{task}' marked as completed!")
    else:
        print("❌ Task not found!")

def delete_task():
    task = input("Enter the task name to delete: ")
    if task in todo_list:
        del todo_list[task]
        print(f"🗑️ Task '{task}' deleted successfully!")
    else:
        print("❌ Task not found!")

def main():
    print("📝 Welcome to the Python To-Do List App!")
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            mark_completed()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            print("\n👋 Exiting To-Do List App. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please select a valid option.")

# Run the program
main()

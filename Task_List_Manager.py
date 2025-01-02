import os

# Function to load tasks from the file
def load_tasks():
    tasks = []
    try:
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                tasks = [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"Error reading the file: {e}")
    return tasks

# Function to save tasks to the file
def save_tasks(tasks):
    try:
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")
    except Exception as e:
        print(f"Error saving to the file: {e}")

# Function to add a task
def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added.")
    else:
        print("Invalid task. Please enter a valid task.")

# Function to remove a completed task
def remove_task(tasks):
    if not tasks:
        print("No tasks available to remove.")
        return
    
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    except IndexError:
        print("Task number out of range.")

# Function to view the current task list
def view_tasks(tasks):
    if tasks:
        print("\nCurrent Task List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("No tasks to display.")

# Main program to manage tasks
def main():
    tasks = load_tasks()
    
    while True:
        print("\nTask List Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Save and Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            save_tasks(tasks)
            print("Tasks saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()

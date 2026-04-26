# To-Do List

tasks = []  #An emplty list

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour tasks:")
        i = 1
        for task in tasks:
            print(f"{i}. {task}")
            i += 1


def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)                       #task -1 , list start from 0. 
            print(f"Deleted: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")

# Main loop
while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")





"""
*Explaning the working of the code:

1.Create a add task function.
2.Create a view task function and apply condition for display.
3.Then add deletion of a list function.
4.After creating every thing above, now write and call all the functions
5.End

"""
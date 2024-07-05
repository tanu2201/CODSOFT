# Initialize an empty list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)

# Function to delete a task
def delete_task(task_number):
    try:
        del tasks[task_number - 1]
    except:
        print("Oh no! It looks like that task doesn't exist. Try again!")

# Function to update a task
def update_task(task_number, new_task):
    try:
        tasks[task_number - 1] = new_task
    except:
        print("Oh no! It looks like that task doesn't exist. Try again!")

# Function to display tasks
def display_tasks():
    if not tasks:
        print("You don't have any tasks yet! Why not add some?")
    else:
        print("Here are your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Main program
while True:
    print("\nWelcome to your task list!")
    print("What would you like to do today?")
    print("1. Add a new task to your list")
    print("2. Remove a task from your list")
    print("3. Update a task on your list")
    print("4. View your tasks")
    print("5. Quit and come back later")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("What's the new task you want to add? ")
        add_task(task)
        print("Task added! You're getting things done!")
    elif choice == "2":
        task_number = int(input("Which task number would you like to delete? "))
        delete_task(task_number)
        print("Task deleted! You're decluttering your list!")
    elif choice == "3":
        task_number = int(input("Which task number would you like to update? "))
        new_task = input("What's the new task? ")
        update_task(task_number, new_task)
        print("Task updated! You're staying on top of things!")
    elif choice == "4":
        display_tasks()
    elif choice == "5":
        print("Goodbye for now! Come back soon to tackle your tasks!")
        break
    else:
        print("Sorry, that's not a valid option. Try again, and I'll help you out!")

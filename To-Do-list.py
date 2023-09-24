todo_list = []
#this adds a task to the list
def add_task(task):
    todo_list.append(task)
    input(f"task '{task}' has been added to the to do list")
#this deletes the task 
def delete_tast(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"task '{task}' has been removed from the todo list")
    else:
        print(f"Task '{task}' is not found in your todo list")
#this function displays all the items in the current todo list       
def display_task():
    if todo_list:
        print('todo list: ')
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
    else:
        print("Your todo list is empty")
#this next set of imputs asks the user what they wish to do 
while True:
    print()
    print("Todo task manager")
    display_task()
    print("\nOptions:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Quit")

    choice = input("Enter what you would like to do! (1/2/3): ")
    
    if choice == '1':
        print()
        task = input("Enter the task you wish to add: ")
        add_task(task)
    elif choice == '2':
        print()
        task = input('Enter the task you wish to remove: ')
        delete_tast(task)
    elif choice == '3':
        confirm = input("Are you sure you want to quit? (yes/no): ").lower()
        if confirm == 'yes':
            print("Goodbye!")
            break
        elif confirm == 'no':
            continue
    else:
        print()
        print("Invalid Choice. plese select a valid option.")

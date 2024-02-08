# Todo-List

def save_task_to_file(tasks, filename="tasks.txt"):
    """ Creates a Txt File to save tasks"""
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task.capitalize() + "\n")

def load_task_from_file(filename="tasks.txt"):
    """Load tasks from file and handle NotFound Error"""
    tasks = []
    try:
        with open(filename, "r") as file:
            tasks = [line.strip() for line in file]
    except FileNotFoundError:
        pass
    return tasks

# Initialization
tasks = load_task_from_file()

# Functions of program

def add_task():
    """ Takes input from user and add it to the task's list"""
    user = input("Enter Task: ").lower().strip()
    if user in tasks:
        print("Task Already Exist")
    else:
        tasks.append(user)
        save_task_to_file(tasks)
        print("\n Task Added Successfully ", end="\n")
    return None

def view_task():
    """  Shows Each Tasks by Number  """
    if not tasks:
        print("No Task to View")
    else:
        print("\n Tasks ")
        # Start = 1. To handle Python indexing from 0 
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.capitalize()}")
    return None

def remove_task():
    """Remove Tasks from List """
    if not tasks:
        print("\n No Task To Remove ")
    else:
        print("\nEnter Task To Remove ")
        for i, task in enumerate(tasks, start =1):
            print(f"{i}. {task.capitalize()}")
            
        try:
            task_num = int(input("Enter Task Number: "))
            if 1 <= task_num <= len(tasks):
                remove = tasks.pop(task_num -1)
                print(f"'{remove.capitalize()}'. Removed Successfully ")
                save_task_to_file(tasks)
            else:
                print("Invalid Task Number ")
                
        except ValueError:
            print(" Enter a Number ")
    return None

def mark_as_completed():
    """ Removes a Task From The list """
    if not tasks:
        print("\n No task to Complete ")
    else:
        print()
        print(" Enter Task to mark as Completed ")
        for i, task in enumerate(tasks, start =1):
            status = " (Completed)" if " (Completed)" in task else ""
            print(f"{i}.{task.capitalize()}")    
        try:
            # Check is the user input in range and mark it as completed 
            complete_task = int(input("Enter Task Number: "))
            if 1 <= complete_task <= len(tasks):
                if " (Completed)" not in tasks[complete_task -1]:
                    tasks[complete_task -1 ] += " (Completed)"
                    print(f"Task '{tasks[complete_task-1].capitalize()}' Marked as Completed ")
                    save_task_to_file(tasks)
                else:
                    print("Task Already Marked ")
            else:
                print("\nInvalid Task Number ")
        except ValueError:
            print("Enter a Valid Number ")
    return None

def clear_all_tasks():
    """ Clear all Task and Return Empty Container """
    if not tasks:
        print(" Nothing To Clear ")
    else:
        while True: # Keep asking until a valid response is given
            clear_all= input(" Are you sure you want to clear all tasks? (y/n): ").lower().strip()
            if clear_all in ["n","no"]:
                break # Exit without clearing the Task 
            elif clear_all in ["y", "yes"]:
                    tasks.clear()
                    save_task_to_file(tasks)
                    print(" All Tasks Has been Deleted")
            else:
                print("Please enter 'y' for yes or 'n' for no.")  # Prompt for valid input
    return None

print("\n Welcome to Todo-List Program ")

def main():
        
    # Main Program
    while True:
        #print("\n Welcome to Todo-List Program ")
        print("\nMenu\n")
        print("*" *15)
        print("1. Add Task")
        print("2. View Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Clear All Tasks")
        print("6. Exit")
        print("*" *15)
        
        choice = input("Enter your Choice: ")
        
        if choice == "6":
            save_task_to_file(tasks)
            break
        elif choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_as_completed()   
        elif choice == "5":
            clear_all_tasks()
        
        else:
            print("\nInvalid Choice ")
        
if __name__ == "__main__":
    main()
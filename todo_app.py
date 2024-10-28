import json  # imports the default JSON module
import os    # imports the os module to interact with the Operating System

TASKS_FILE = 'tasks.json'  # Defines where to store the tasks.

def banner():
    """Displays the banner for the To-Do List application."""
    print("""
========================================================================================
  _______    ____             _____     ____          _        _____    _____   _______ 
 |__   __|  / __ \           |  __ \   / __ \        | |      |_   _|  / ____| |__   __|
    | |    | |  | |  ______  | |  | | | |  | |       | |        | |   | (___      | |   
    | |    | |  | | |______| | |  | | | |  | |       | |        | |    \___ \     | |   
    | |    | |__| |          | |__| | | |__| |       | |____   _| |_   ____) |    | |   
    |_|     \____/           |_____/   \____/        |______| |_____| |_____/     |_|   
          
========================================================================================                                                                                     
To Do List | A Python-powered To-Do List.
By Eoghan (2024).
=========================================================================================
""")  # Displays the generated to-do list banner in ASCII and prints it.


def load_tasks():
    """Loads tasks from the tasks.json file and returns the list of tasks."""
    try:
        if os.path.exists(TASKS_FILE):  # Check if the file exists
            with open(TASKS_FILE, 'r') as file:
                return json.load(file)  # Load the list from the JSON file
        return []  # Return an empty list if the file doesn't exist
    except (FileNotFoundError, json.JSONDecodeError) as e: # Catches any errors related to file access.
        print(f"Error loading tasks from {TASKS_FILE}: {e}") #Prints an error message
        return []  # Return an empty list on the error.

def save_tasks(tasks):
    """Saves the current tasks to the tasks.json file."""
    try:
        with open(TASKS_FILE, 'w') as file: #opens the JSON file in write mode.
            json.dump(tasks, file, indent=4)  # Writes tasks into JSON format
    except Exception as e:   # Catch any exceptions that occur during file writing
        print(f"An error has occurred while saving the tasks: {e}")   #prints the error message

def add_task(tasks, description, status='pending'):
    """Adds a new task to memory with a description and status to the task list."""
    task = {        # Creates a new dictionary called 'task'
        'Description': description,       #Creates a new object string within task dictionary called 'Description.' with the value description  
        'Status': status                   #Creates a new object string within task dictionary called 'status', with the value status.
    }   #Closed parenthesis for the tasks dictionary
    tasks.append(task)                  # Append the new task to the list of tasks
    save_tasks(tasks)             #saves tasks to JSON file.

#View tasks funtion for the app to handle viewing tasks
def view_tasks(tasks):          
    """Displays all tasks in the list with their descriptions and statuses."""
    if not tasks:            #Checks if the task list is empty
        print("No tasks available. Start a new task...")    #Prints prompt to user to add a task
        return
    #For loop that indexes the tasks in a range
    for i in range(len(tasks)):
        task = tasks[i]     
        print(f"{i + 1}. {task['Description']} - {task['Status']}")  #Prints an f string function with the function 'i + 1' {task['Description']} and {task['Status']} accesses the value from the key associated with description and status within the tasks dictionary.


def update_task(tasks, task_id, new_description=None, new_status=None):
    """Updates the description and/or status of a specified task."""
    try:
        task = tasks[task_id - 1]
        if new_description:
            task['Description'] = new_description  # Update the correct key
        if new_status:
            task['Status'] = new_status  # Update the correct key
        save_tasks(tasks)
    except IndexError:
        print("Error: Task ID does not exist.")
    except Exception as e:
        print(f"An error occurred while updating the task: {e}")

def delete_task(tasks, task_id):
    """Deletes a specified task from the tasks list."""
    try:
        tasks.pop(task_id - 1)  # Remove the task
        save_tasks(tasks)
    except IndexError:
        print("Error: Task ID does not exist.")
    except Exception as e:
        print(f"An error occurred while deleting the task: {e}")

def get_task_id(prompt, tasks):
    """Prompts the user for a task ID and validates the input."""
    while True:
        try:
            task_id = int(input(prompt))
            if 1 <= task_id <= len(tasks):
                return task_id
            else:
                print("Error: Please enter a valid task ID.")
        except ValueError:
            print("Error: Please enter a number.")

def main():
    """Main function of To-Do List application."""
    tasks = load_tasks()  # Load existing tasks from tasks.json
    banner()  # Show the banner

    while True:
        # Main menu options
        print("\nTo-Do List menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        user_choice = input("Choose an option: ")

        if user_choice == '1':
            description = input('Add task description: ')
            add_task(tasks, description)
        
        elif user_choice == '2':
            view_tasks(tasks)
        
        elif user_choice == '3':
            view_tasks(tasks)
            task_id = get_task_id("Enter the task ID to update: ", tasks)
            new_description = input("Enter new description (leave blank to keep current): ")
            new_status = input("Enter new status (leave blank to keep current): ")
            update_task(tasks, task_id, new_description or None, new_status or None)
        
        elif user_choice == '4':
            view_tasks(tasks)
            task_id = get_task_id("Enter the task ID to delete: ", tasks)
            delete_task(tasks, task_id)
        
        elif user_choice == '5':
            print("Exiting the To-Do List application.")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()  # Run the main function

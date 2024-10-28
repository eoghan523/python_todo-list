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

# Function to handle updating of tasks.
def update_task(tasks, task_id, new_description=None, new_status=None): 
    """Updates the description and/or status of a specified task."""
    try:  #Try except logic block to handle updating tasks
        task = tasks[task_id - 1]    # Access the task by its ID
        if new_description:           # Update the task's description with the new value
            task['Description'] = new_description  # Update the correct key 
        if new_status:          # Update the task's status with the new value
            task['Status'] = new_status  # Update the correct key
        save_tasks(tasks)          #Saves tasks to JSON file
    except IndexError:   #except catch to handle any instance where the task ID does not correspond to any task
        print("Error: Task ID does not exist.")
    except Exception as e:        # Handle any other exceptions that may occur and print the error message
        print(f"An error occurred while updating the task: {e}")   #Prints eerror message for the user.  A {e} placeholder to embed the value of e in the string.

#function to handle the deleting of tasks and task ids.
def delete_task(tasks, task_id):
    """Deletes a specified task from the tasks list."""
    try:  #try excetionn logic block to handle the delete task functions.
        tasks.pop(task_id - 1)  # Remove the task using .pop() function.
        save_tasks(tasks)       ## Save the updated task list to the JSON file
    except IndexError:   #except catch to handle indexing error
        print("Error: Task ID does not exist.") #prints error for the user task Id dosent exist
    except Exception as e:    #Another except catch to handle exceptions
        print(f"An error occurred while deleting the task: {e}") #prints an f string with the error message. A {e} placeholder to embed the value of e in the string.

#This function get task id is defined to to handle and validate user input. 
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

        user_choice = input("Choose an option: ") #Defining the user_choice variable and giving it the value of input.
#This If/elif/else block forms the main logic function of the menu list. 

        #If the users input is the value equal to '1' then... 
        if user_choice == '1':
            description = input('Add task description: ') #input into the description
            add_task(tasks, description) #adds task to 
        
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

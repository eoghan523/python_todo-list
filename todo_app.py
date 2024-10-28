import json  # imports the default JSON module
import os    # imports the os module to interact with the Operating System

TASKS_FILE = 'tasks.json'  # Defines where to store the tasks.

def banner():
    """Displays the banner for the To-Do List application."""
    print(r"""
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
    task_id = len(tasks) + 1  # Generates  a unique task ID
    task = {        # Creates a new dictionary called 'task'
        'id'       :  task_id,  #adds task id to the task dictionary
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

     # Starts a loop to repeatedly prompt for valid input
    while True:
        try:
            # Asks the user to enter a task ID, converting the input to an integer
            task_id = int(input(prompt))
              # Checks to see if the entered ID is within the valid range.
            if 1 <= task_id <= len(tasks):
                return task_id    # Returns the valid task ID
            else:
                #Esle catch for werror handling 
                print("Error: Please enter a valid task ID.") #Prints error promting the user to enter a valid task ID.
        except ValueError:       #Except catch to handle any value error inputs. 
            print("Error: Please enter a number.") #Prints message to prompt user to enter a number.

#The main function of the To-DO app.
def main():
    """Main function of To-Do List application."""
    tasks = load_tasks()  # Load existing tasks from tasks.json
    banner() # Call the banner function to display the application banner
  
    while True:   # Start an infinite loop to continuously display the menu until the user adds input or exits the application.
        
        # Main menu options
        print("\nTo-Do List menu:")   # Print a newline and the menu title.
        print("1. Add Task")          # Print the option to add a task.
        print("2. View Tasks")        # Print the option to view existing tasks.
        print("3. Update Task")       # Print the option to update a specific task.
        print("4. Delete Task")       # Print the option to delete a task.
        print("5. Exit")              # Print the option to exit the application.

        user_choice = input("Choose an option: ") #Defining the user_choice variable and giving it the value of input. This line of code will promt the user for input

        #This If/elif/else block forms the main logic function of the menu list. It guides the user selection.

        #If the users input is the value equal to '1' then... 
        if user_choice == '1':
            description = input('Add task description: ') #Promt for the user to add a task description
            add_task(tasks, description)                 # Call the add_task function to add the new task with the provided description.
        
        elif user_choice == '2':      #if user selcts 2
            view_tasks(tasks)       # This line of cod Calls the view_tasks function to display all current tasks.
        
        elif user_choice == '3': #If users input is equal to 3 
            view_tasks(tasks)    # Display current tasks so the user knows which one to update.
            task_id = get_task_id("Enter the task ID to update: ", tasks)     # Get the task ID to update from the user.
            new_description = input("Enter new description (leave blank to keep current): ")   # Prompt for a new description or leave blank for no change.
            new_status = input("Enter new status (leave blank to keep current): ")             #Promt for the user to add new status or leave blank to keep its status as pending.
            update_task(tasks, task_id, new_description or None, new_status or None)          # Call update_task with new values or 'none' if the input is left blank.
        
        elif user_choice == '4':       #If the input is equal to '4'
            view_tasks(tasks)          # Display the current tasks in memory for the user to select
            task_id = get_task_id("Enter the task ID to delete: ", tasks)  #Get the task id forr the user to delete.
            delete_task(tasks, task_id)     # Call delete_task to remove the selected task.
        
        elif user_choice == '5':      #if users input is equal to 5
            print("Exiting the To-Do List application.")   #Print string to pompt the user to exit the todo app
            break   #Break will exit the while loop function.
        
        else:
            print("Invalid option. Please try again.")    #The elso catch will catch any user input errorr that is not a valid input.

# This line of code checks if the script is being run directly and not an imported module.
if __name__ == "__main__":
    main()  # Run the main function to start the application

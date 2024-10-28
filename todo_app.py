import json     #imports the default JSON module
import os       #This import the os module so you can interact with the Operating System.


TASKS_FILE = 'tasks.json' #This line of code defines where to store the tasks.

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
                                                                                         
To Do List | A Python-powered To-Do List.
By Eoghan (2024).
=========================================================================================
""")    #This function banner () displays the generated to do list banner in ascii and prints it. 
    
def load_tasks():
    """Loads tasks from the tasks.json file and returns the list of tasks"""
    try:
        #Try except block that checks if the tasks file actually exists in the specified location
        if os.path.exists(TASKS_FILE): #If the file exists, open the file in read mode 
            with open(TASKS_FILE, 'r')as file: 
                #load the list from the JSON file the list of tasks
                return json.load(file)
                #If it dosent exist, return the file as empty
        return[]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        #Except block to handle to error of missing file/ coding error.
        print(f"Error loading tasks from {TASKS_FILE}: {e}")
        #Return an empty list 
        return[]

#Save tasks function to the tasks.json file
def save_tasks(tasks):
    """Saves the current tasks to the tasks.json file."""
    try:
        with open(TASKS_FILE, 'w')as file:
            json.dump(tasks, file, indent=4) #json.dump() writes tasks into json format. 'Indent=4' makes the json file into a more user readable format.
    
    except Exception as e:
        print(f"An error has occured whilst saving the tasks: {e}")

#Add new task fuction
def add_task(tasks, description, status='pending'):
    """Adds a new task to memory with a simple description and status to the task list."""
    
    task = {
        'Description': description,
        'Status'     : status
            
    }
    tasks.append(tasks)
    save_tasks(tasks)

#view tasks
def
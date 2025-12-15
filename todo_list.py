"""
Simple ToDo List Application
----------------------------
This is a command-line ToDo List program that allows a user to:

1. Add new tasks
2. View all tasks
3. Remove a task by its number
4. Edit a task by its number
5. Exit the application

The program ensures safe input handling  
and prevents adding empty tasks.
"""

# Global list that stores all tasks
todo_list = []

# Todo List Methods
def check_tasks():
    """
    Check if there are tasks in the todo_list.
    
    Returns:
        bool: True if there are tasks, False otherwise.
    """
    return bool(todo_list)

def todo_add(task):
    """
    Add a new task to the todo_list.
    
    Parameters:
        task (str): The task text to be added.
        
    Notes:
    - Ignores empty tasks.
    """
    if not task:
        print("Empty task not added.")
        return
    todo_list.append(task)
    print(f'task ({task}) added successfully')


def todo_view():
    """
    Display all tasks in the todo_list.
    
    Notes:
        - Shows tasks as a numbered list starting from 1.
        - If no tasks exist, displays a message instead.
    """
    if not todo_list:
        print('No tasks to view. Please add a task first.')
    else:
        print('Your tasks are:')
        for index, task in enumerate(todo_list, start=1):
            print(f'{index}. {task}')


def todo_remove():
    """
    Remove a task from the todo_list by its number.
    
    Workflow:
        - Displays all tasks with numbers.
        - Asks the user for a number input.
        - Validates that input is a digit and within the valid range.
        - Removes the corresponding task if valid.
    """
    if not todo_list:
        print('No tasks to remove. Please add a task first.')
        return

    print('Your tasks are:')
    for index, task in enumerate(todo_list, start=1):
        print(f'{index}. {task}')

    choice = input('Enter the NUMBER of the task you want to remove: ')
    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    task_numb = int(choice)
    if 1 <= task_numb <= len(todo_list):
        removed_task = todo_list.pop(task_numb - 1)
        print(f'task ({removed_task}) removed successfully')
    else:
        print("Invalid number, no task removed.")


def todo_edit():
    """
    Edit an existing task in the todo_list.
    
    Workflow:
        - Displays all tasks with numbers.
        - Asks the user for a number input.
        - Validates that input is a digit and within the valid range.
        - Prompts for new task text.
        - Updates the task if valid and not empty.
    """
    if not todo_list:
        print('No tasks to edit. Please add a task first.')
        return

    print('Your tasks are:')
    for index, task in enumerate(todo_list, start=1):
        print(f'{index}. {task}')

    choice = input('Enter the NUMBER of the task you want to edit: ')
    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    task_numb = int(choice)
    if 1 <= task_numb <= len(todo_list):
        old_task = todo_list[task_numb - 1]
        new_task = input(f'Enter the new text for task ({old_task}): ').strip()
        if not new_task:
            print("Empty task not added.")
            return
        todo_list[task_numb - 1] = new_task
        print(f'task ({old_task}) updated to ({new_task}) successfully')
    else:
        print("Invalid number, no task edited.")



# -------------------------------
# Main program loop
# -------------------------------
print('Welcome to the simple ToDo List. Let\'s start:')

while True:
    choice = input(
        'Choose a number from the list: ([1] Add , [2] View , [3] Remove , [4] Edit , [5] Exit): '
    )

    if not choice.isdigit():
        print('Invalid command. Please enter a number between 1 and 5.')
        continue

    user_input = int(choice)

    if user_input == 1:
        task = input('Enter the task you want to add: ').strip()   #Strips leading/trailing spaces.
        todo_add(task)
    elif user_input == 2:
        todo_view()
    elif user_input == 3:
        todo_remove()
    elif user_input == 4:
        todo_edit()
    elif user_input == 5:
        print('Exiting the ToDo List application. Goodbye!')
        break
    else:
        print('Invalid command. Please choose a valid number from the list.')

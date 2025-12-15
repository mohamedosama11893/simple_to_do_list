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

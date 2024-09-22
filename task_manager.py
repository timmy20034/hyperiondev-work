from datetime import datetime

# Specify the path to the user file
file_path = "user.txt"
filename = "tasks.txt"
def add_task():
    # Asking for task information
    task_user = input("Please type the user the task is for:\n")
    task_title = input("What is the title of the task?:\n")
    task_description = input("Please write the description of the task:\n")
    task_duedate = input("When is the task due? (DD MMM YYYY):\n")
    task_currentdate = datetime.now().strftime("%d %b %Y")
    task_complete = input("Is the task complete (Yes or No):\n")

    # Condensing the infomation to put into the file
    task_data = (
    f"{task_user}, "
    f"{task_title}, "
    f"{task_description}, "
    f"{task_duedate}, "
    f"{task_currentdate}, "
    f"{task_complete}"
)

    # Writing it to file
    with open("tasks.txt", "a") as file:
        file.write("\n" + task_data)
    
    # Conformation that it was added to file
    print("Task added successfully!")

def read_users_from_file(file_path):
    users = {}
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            for line in file:
                # Split each line by comma to get username and password
                username, password = line.strip().split(', ')
                users[username] = password
    except FileNotFoundError:
        print(f"{file_path} not found.")
    return users

logged_in_user = ""

def login(file_path):
    global logged_in_user
    users = read_users_from_file(file_path)
    
    while True:
        username = input("Enter username:\n")
        password = input("Enter password:\n")
        
        # Check if credentials are valid
        if username in users and users[username] == password:
            print("Login successful!")
            logged_in_user = username
            break
        else:
            print("Invalid username or password. Please try again.")

def start_menu():
    # Present the menu to the user and 
    global menu
    menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()
# A function to count the users           
def count_users(file_path):
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []
# A funciton to count tasks    
def count_tasks(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            tasks = file.readlines()
            return len(tasks)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return 0
            
def start_menu_admin():
    global menu
    menu = input('''Select one of the following options:          
r - register a user
vu - view number of users                  
a - add task
va - view all tasks
vm - view my tasks
vt - view total number of tasks                 
e - exit
: ''').lower() 
# Function to check if input is just blank
def is_blank(input_str):
    return not input_str.strip()
# Fuction to check if a user already excits
def user_exists(username, filename='user.txt'):
    try:
        with open(filename, 'r') as f:
            for line in f:
                existing_user, _ = line.strip().split(', ')
                if existing_user == username:
                    return True
        return False
    except FileNotFoundError:
        # If the file doesn't exist, we assume no users exist yet
        return False
    except Exception as e:
        print(f"An error occurred while checking if user exists: {e}")
        return False

def process_tasks(filename, encoding='utf-8'):
    try:
        with open(filename, 'r', encoding=encoding) as to_do:
            for line in to_do:
                     # Split the line at the comma and space
                    task_parts = line.strip().split(', ')
                    
                    # Check if the line has the correct number of parts
                    if len(task_parts) != 6:
                        raise ValueError(
                            "Line does not have the expected number of parts.")
                    
                    # Printing the file in a format easy to read
                    print("Task:           " + task_parts[1])
                    print("Assigned to:    " + task_parts[0])
                    print("Date assigned:  " + task_parts[4])
                    print("Due date:       " + task_parts[3])
                    print("Task Complete?  " + task_parts[5])
                    print("Task description:\n" + task_parts[2])
                
    except ValueError as e:
        print(f"Skipping line due to error: {e}")
    except IndexError as e:
        print(f"Skipping line due to missing data: {e}")

    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")

def process_user_tasks(logged_in_user, filename, encoding='utf-8'):
    tasks_found = False
    
    try:
        with open(filename, 'r', encoding=encoding) as to_do:
            for line in to_do:
                    # Split the line at the comma and space
                    task_parts = line.strip().split(', ')
                    
                    # Check if the line has the correct number of parts
                    if len(task_parts) != 6:
                        raise ValueError(
                            "Line does not have the expected number of parts.")
                    
                    # Filters tasks by the current user
                    if task_parts[0] == logged_in_user:
                        tasks_found = True
                        
                        # Printing the file in a format easy to read
                        print("Task:           " + task_parts[1])
                        print("Assigned to:    " + task_parts[0])
                        print("Date assigned:  " + task_parts[4])
                        print("Due date:       " + task_parts[3])
                        print("Task Complete?  " + task_parts[5])
                        print("Task description:\n" + task_parts[2])
                
    except ValueError as e:
        print(f"Skipping line due to error: {e}")
    except IndexError as e:
        print(f"Skipping line due to missing data: {e}")

    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    
    if not tasks_found:
        print("You currently have no tasks.")

# Run the login function
login(file_path)

while True:
    if logged_in_user == "admin":
        start_menu_admin()

    else:
        start_menu()

    if menu == 'r':
        # Asking for new user and password 
        
        if logged_in_user == "admin":
            
            while True:
                new_user = input("Please enter username:\n").strip()
                if is_blank(new_user):
                    print("Username cannot be blank. Please try again.")
                    continue
                if user_exists(new_user):
                    print("Username already exists. Please try again.")
                    continue
                new_password = input("Please enter password:\n").strip()
                confirm_password = input(
                    "Please confirm your password:\n").strip()                 
                if is_blank(new_password):
                    print("Password cannot be blank. Please try again.")
                    continue
                if new_password != confirm_password:
                    print("Passwords do not match. Please try again.")
                else:
                    try:
                        with open("user.txt", "a") as f:
                            f.write("\n" + new_user + ", " + new_password)
                        print("User added successfully!")
                        break
                    except Exception as e:
                        print(f"An error occurred while adding the user: {e}")

        else:
            print("Only Admin can do this")

    elif menu == "vu":
        print("Current Users", + count_users(file_path))

    elif menu == 'a':
        # Fuction 
        add_task()

    elif menu == 'va':
        process_tasks(filename)
        
    elif menu == 'vm':
        process_user_tasks(logged_in_user, filename)

    elif menu == "vt":  
        print("Current Tasks", + count_tasks(filename))

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")
      
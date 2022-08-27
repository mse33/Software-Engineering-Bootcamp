# Import current time and date:
import datetime

# Define a function to register a new user: 
def reg_user():
    # Open file:
    with open("user.txt" , "a+") as file:
        # Ask for username
        new_user = input("Please enter a username: ").lower()
        # If it exists user muct chose another:
        while new_user in usernames:
            print("This username exists already. Please enter a different one")            
            return reg_user()
        
        # User must enter their password twice to avoid errors
        new_pass = input("Please enter a password: ").lower()        
        confirm_pass = input("Please re enter your password: ").lower()

        # Verify that the password are identical
        if new_pass == confirm_pass:
            # Write new user to file
            file.write( f"\n + {new_user}, {new_pass}")
            
        print("The new user has been registered!")
        
    while new_pass != confirm_pass:
         print("Paswords don't match. Try again")
         # Ask for user to enter passwords again:
         new_pass = input("Please enter a password: ").lower()        
         confirm_pass = input("Please re enter your password: ").lower()
            
         # only append to the file if password are identical 
         if new_pass == confirm_pass:
                # Add user to file:                
                file.write( f"\n + {new_user}, {new_pass}")

# Define a function to add a new task:
def add_task():
        # Open file:
        with open("user.txt" , "a+") as file:
            
            # Ask for task details:
            user_name = input("Enter the username of the task assignee: ")
            task_name = input("Enter task name: ")
            task_description = input("Enter a task description: ")
            task_date = input("Enter task due date: eg. 2022-03-09:  ")
            
            today_date = datetime.date.today()
            task_completion_status = "No"
            
            # Write new task to file:
            file.writelines(f"\n {user_name}, {task_name}, {task_description}, {task_date}, {today_date}, {task_completion_status}")
            print("Task created and added!")
        # Close file:   
        file.close()

# View all tasks:
def view_all():
        
        with open("tasks.txt" , "r") as file:
            # List from file data
            all_tasks = [line.strip().split(", ") for line in file]
            # Display data to user:
            for items in all_tasks:
                print(f'''
                Task:                   {items[1]}
                Assigned to:            {items[0]}
                Date assigned:          {items[2]}
                Task due date:          {items[4]}
                Task completion status: {items[5]}
                Task Description:       {items[2]} ''')
                
        # Close file   
        file.close()


# Function to display user specific information:
def view_mine():
    
    # Create empty dictionary and counter:
    dict_tasks = {}   
    num_tasks = 0
    
    # Open and read file:
    with open("tasks.txt" , "r+") as file:
        
            # Add data into a list: 
            for tasks in file:
                items = tasks.strip("\n").split(", ")
                
                # Count number of tasks:
                num_tasks += 1                
                dict_tasks[num_tasks] = items
            
                # If the username entered matches the Assigned to section then it diplays all the tasks specific to them 
                if user_name == items[0]:
                    print(f'''
                    Task:                   {items[1]}
                    Assigned to:            {items[0]}
                    Date assigned:          {items[2]}
                    Task due date:          {items[4]}
                    Task completion status: {items[5]}
                    Task Description:       {items[2]} ''')
                                                 
                # Does user want to edit a task?
                task_num = int(input("""
                    If you would like to edit a task enter the task number
                    
                    Enter -1 if you would like to exit"""))
                
                # Special menu to edit tasks:
                if task_num in dict_tasks:
                    update_task = int(input("""
                    Select one of the following actions:
                        u    Change person assigned to task
                        d    Change deadline of task 
                        c    Update status to Complete"""))
                        
                    # Ensure only incomplete tasks can be altered:    
                    if dict_tasks[task_num][-1] == "No":
                        if update_task == "u":
                            # Assign task to different user:
                            dict_tasks[task_num][0] = input("Please enter new user: ")
                            print("The Task Asignee has been updated!")
                            
                        elif update_task == "d":
                            # Edit the deadline:
                            dict_tasks[task_num][-2] = input("Please enter new Deadline: eg. 2000-08-04 ")
                            print("Due date updated!")
                            
                        elif update_task == "c":
                            # Complete task:
                            dict_tasks[task_num][-1] = "Yes"
                            print("Task Complete!")
                            
                    else:
                        print("Error. Only Incomplete tasks can be modified. ")
                # Back to previous menu:       
                elif task_num == -1:
                    return
                # New string with altered info
                updated_task = "\n".join([", ".join(t) for t in dict_tasks.values()])
                # Open and write to file: 
                with open("tasks.txt" , "w") as file:
                    file.write(updated_task)
                    
def task_overview():
    
    # Empty dictionary:
    task_dict = {}
    
    # Seta all counters to zero:
    completed = 0
    incomplete = 0
    overdue = 0 
    task_count = 0
    
    # Open and read tasks file:
    with open("tasks.txt" , "r+") as file2:       
        for list in file2:
            lines = list.strip("\n").split(", ")
            
            # Count lines:
            task_count += 1            
            task_dict[task_count] = lines
    
    # Create and write to task_overview file:
    with open("task_overview.txt" , "w") as file:
        
        for count in task_dict:           
            task = task_dict[count]
            
            if task[-1] == "Yes":
                completed += 1
                
            elif task[-1] == "No":
                incomplete += 1
                
            task_date = datetime.datetime.strptime(task[4], '%Y-%m-%d')
            # Determine which tasks are overdue:
            if task_date < datetime.datetime.today() and task[-1] == "No":
                
                overdue += 1
                
        # Determine percentages for overdue and incomplete tasks:       
        percentage_incomplete = round(((incomplete/task_count)*100), 2)
        percentage_overdue = round(((overdue/task_count)*100), 2)
        
        # Write data to the file using an f string:
        file.writelines(f""" The current number of Tasks is {task_count}. Thus far, {completed} are finished and {incomplete} are incomplete.
                        Currently {overdue} are overdue. Overall,{percentage_incomplete}% of tasks are incomplete and {percentage_overdue}% are overdue.""")
   
def user():
    # Empty user list:
    users = []
    
    # Open and read user file:
    with open("user.txt", "r+") as f:
        for line in f:
            
            all_users = line.strip("\n").split(", ")
            # Enter data into dictionary
            users.append(all_users[0])
            
    # return function:
    return users
                            
                            
# Function to create user specific reports:                            
def each_user(user_name, task_dict):
    
    # Empty counters for all of the stats
    user_tasks = 0
    completed_tasks = 0
    incomplete_tasks = 0
    overdue_tasks = 0
    total_tasks = 0
    task_percentage = 0
    complete_percent = 0
    incomplete_percent = 0
    overdue_percent = 0
    
    
    with open("tasks.txt" , "r") as files:
        
        # Calcutate all of the staistics:
        for count in task_dict:
            task = task_dict[count]
            total_tasks  += 1
            
            if user_name == task[0]:
                user_tasks += 1
            if user_name == task[0] and task[5] == "Yes":
                completed_tasks += 1
            if user_name == task[0] and task[5] == "No":
                incomplete_tasks += 1
             
            # Due date:
            due_date = datetime.datetime.strptime(task[4], '%Y-%m-%d')
            
            # Determine whether the task is overdue:
            if user_name == task[0] and due_date < datetime.datetime.today() and task[-1] == "No":
                overdue_tasks += 1
                
    # Generate percentages of statistics:           
    if user_tasks != 0:
        # Make sure the values have been rounded:
        complete_percent = round(((completed_tasks/user_tasks)*100), 2)
        incomplete_percent = round(((incomplete_tasks/user_tasks)*100), 2)
        overdue_percent = round(((overdue_tasks/user_tasks)*100), 2)
        task_percentage = round(((user_tasks/total_tasks)*100), 2)
    
    # Display the Statistics neatly using an f string:
    return f""" \n User; {user_name}
                \n Total Tasks {total_tasks}
                \n User tasks: {user_tasks}
                {user_name} tasks = {task_percentage}% of all tasks
                {incomplete_percent}% of {user_name}'s tasks not completed.
                {complete_percent}% of {user_name}'s tasks completed.
                {overdue_percent}% of {user_name}'s tasks overdue."""
                        
                
def user_overview():
    
    # Empty task dictionary:
    task_dict = {}
    users = user()
    
    # Count the number of users using len():
    total_users = len(users)
    
    # Set counter to zero:
    task_count = 0
    
    # Open and read tasks file:
    with open("tasks.txt" , "r") as file2:
        for list in file2:
            # Create a list:
            lines = list.strip("\n").split(", ")
            # Count lines in file:
            task_count += 1
            task_dict[task_count] = lines
            
        user_data = ""
        
        for u in users:
            user_data += each_user(u, task_dict)
            
    # Write data to file:
    with open("user_overview.txt", "w") as file:
        file.write(f"""There are {total_users}  users.
                   There are {task_count} tasks.""")
        file.write("\n")
        file.write(user_data)
        
# Define a function to draw up reports:       
def gen_reports():
    task_overview()
    user_overview()
    return print("Reports generated: Take a look in task_overview.txt")

print("Welcome to the Task Management Program!!!")

# Boolean:
valid = True 
# Empty usernames dictionary:    
usernames = {}
# Empty passwords dictionary
passwords = {}

# read the text files and enter the data into the dictionaries defined above
with open("user.txt" , "r+") as file:
    
    # Loop through the lines in the file:
    for lines in file:
        
        data = lines.strip("\n").split(", ")
        
        # Assign a key and a value by indexing 
        usernames[data[0]] = data[1]
        
        passwords[data[1]] = data[0]
     
    # Close file:
    file.close()
        

# While loop to verify username and account details:    
while valid:
    
    # Prompt user to enter their username and their password:
    user_name = input("Enter your username: ")
    password = input("Enter your password: ")
    
   
    # if statement to check if user input is present in the txt file:
    if user_name in usernames and password == usernames[user_name]:
        valid = False
        
        
# Display a special menu to the Admin of the program:     
while True:

    if user_name == "admin":
        
        # Ask admin to choose from the menu:
        menu = input(""" 
        Select one of the actions below:             
        r    Register a new user
        a    Add a task
        va   view all tasks 
        vm   view my tasks 
        gr   gererate reports
        s    show statistics 
        e    exit
         """).lower()

    # All the users who are not Admin see a different menu 
    else:
        
        # Ask user to select an action:
        menu = input("""
                     Select an action below: 
                    a   Add a task
                    va  view all tasks
                    vm  view my tasks 
                    e   exit
                     """).lower()
        
                     
      
    # Allow only the Admin to register a new user:   
    if menu == "r" and user_name == "admin":
        reg_user()

    
     # Add new task:       
    elif menu == "a":
        add_task()
  
    # View all tasks:
    elif menu == "va":
        view_all()
        
 

    # View all user specific tasks:   
    elif menu == "vm":
        view_mine()
        

         # Open the tasks file and read from it: 
        with open("tasks.txt" , "r+") as file:
            

            # Create a list of the tasks 
            tasks = [line.strip().split(", ") for line in file]
            
      

            # For loop to display tasks specific to the user 
            for items in tasks:
                
                # Check username: 
                if user_name == items[0]:
                    
                    # Print the task info in a readable format:
                    print(f'''
                    Task:                   {items[1]}
                    Assigned to:            {items[0]}
                    Date assigned:          {items[2]}
                    Task due date:          {items[4]}
                    Task completion status: {items[5]}
                    Task Description:       {items[2]} ''')
                    
                # Break loop:                                
                break
            
            # Close file:
            file.close()
            
    # Next elif statement if Admin user wants to view statistics:
    elif menu == "s" and user_name == "admin":
        gen_reports()
        
        print("Reports for users:")

        # open the file and read it with a for loop
        with open("user.txt" , "r+") as first_file:
            
            for line in first_file:
                print(line)
            
          
        first_file.close()
        
        print("Reports for tasks:")
        # Open second file and loop through it to count the number of tasks 
        with open("tasks.txt", "r+") as file2:
            
            for info in file2:
                print(info)
        
        # Close file:
        file2.close()
        
     # Generate reports:   
    elif menu == "gr":
        # Call function:
        gen_reports()
        
    # Exit the program if user selects e: 
    elif menu == "e":
        print("Program terminated")
        exit()

    # Else statement in case of invalid input: 
    else:
        print("Error. Please enter a valid option. ")
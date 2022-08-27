'''The following program has been designed to be a task management program for a small company 
Import current time and date '''

from datetime import date
today = date.today()
print("Welcome to the Task Management Program!!!\n")
valid = True

# Create an empty dictionary for usernames
usernames = {}
# create another empty dictionary for the passwords
passwords = {}


'''Open and read the text files and enter the data into the two dictionaries defined above
 Loop through the lines in the file to achieve this.'''
with open("user.txt" , "r+") as file:
    for lines in file:
        
        data = lines.strip("\n").split(", ")
        
        # Assign a key and a value by indexing
        usernames[data[0]] = data[-1]
        
        passwords[data[-1]] = data[0]
        
    
        
 



# While loop to verify username and account details     
while valid:
    
    # Prompt user to enter their username and their password
    user_name = input("Enter your username: ")
    password = input("Enter your password: ")
    
    # if statement to confirm that their login details are in the txt file
    if user_name in usernames and password == usernames[user_name]:
        valid = False
        
        
''' While loop that will display a special menu to the Admin of the program
        Ask which action they would like to select         '''
        
while True:

    if user_name == "admin":
        
        # Display menu:
        menu = input(""" 
        Secect one of the actions below:             
        r    Register a new user
        a    Add a task
        va   view all tasks 
        vm   view my tasks 
        s    show statistics 
        e    exit
         """).lower()
        # .lower function to remove input errors 



    else:
        # Display the menu to users who are not the Admin
        menu = input("""
                     Select an action below: 
                    a   Add a task
                    va  view all tasks
                    vm  view my tasks 
                    e   exit
                     """).lower()
        
                     
    # Verify that a user is admin if they want to register a new user:       
    if menu == "r" and user_name == "admin":
        
        # Open the users file and append a new user and a new password 
        with open("user.txt" , "a+") as file:
            
            '''Ask user for the new username and password 
            Then ask them to confirm their password   '''          
            
            new_user = input("Please enter a username: ").lower()
            new_pass = input("Please enter a password: ")
            
            confirm_pass = input("Please re enter your password: ")
            
            ''' If statement to check if their first and second passwords match
             If they match append the data to the file '''
            
            if new_pass == confirm_pass:
                file.write("\n")
                file.write(f"\n{new_user} , {new_pass}")
                
        # While loop to promp the user for the correct input if their first and second passwords do not match                 
                
        while new_pass != confirm_pass:
        
            print("Paswords don't match. Try again")
        
            new_pass = input("Please enter a password: ").lower()
        
            confirm_pass = input("Please re enter your password: ").lower()
            
            # only append to the file if the passwords match 
        
            if new_pass == confirm_pass:
                
                
                file.write( f"\n  {new_user}, {new_pass}")
                
            
    # Elif statement if user chooses to create a new task        
    elif menu == "a":
        
        # Open file and ask for the task information
        with open("tasks.txt" , "a+") as file:
            
            user_name = input("Enter the username of the task assignee: ")
            
            task_name = input("Enter task name: ")
            
            task_description = input("Enter a task description: ")
            
            task_date = input("Enter task due date: ")
            
            todayDate = today
            task_completion_status = "No"
      
                   
            file.writelines(f"\n{user_name} , {task_name}, {task_description}, {task_date}, {todayDate}, {task_completion_status}")
            
            break
        file.close()
        
   


    # Elif statement to execute code if user selects va:
    elif menu == "va":
        with open("tasks.txt", "r+") as file:
            
            all_tasks = [line.strip().split(", ") for line in file]
            
            # Display the code in desired format using f string
            for items in all_tasks:
                print(f'''
                Task:                   {items[1]}
                Assigned to:            {items[0]}
                Date assigned:          {items[2]}
                Task due date:          {items[4]}
                Task completion status: {items[5]}
                Task Description:       {items[2]} ''')
                
            break
        file.close()



        
    elif menu == "vm":
        
        # Open the tasks file and read from it 
        with open("tasks.txt" , "r+") as file:
            
            # Create a list of the tasks 
            tasks = [line.strip().split(", ") for line in file]
            


            # For loop to display tasks specific to the user
            for items in tasks:
                if user_name == items[0]:
                    print(f'''
                    Task:                   {items[1]}
                    Assigned to:            {items[0]}
                    Date assigned:          {items[2]}
                    Task due date:          {items[4]}
                    Task completion status: {items[5]}
                    Task Description:       {items[2]} ''')
                                                 
                break
            file.close()
            
    # Next elif statement if Admin user wants to view the statistics      
    elif menu == "s" and user_name == "admin":
        
        
    
        
        # open the file and read it
        with open("user.txt" , "r+") as first_file:
            
           num_users = len(first_file.readlines())
           # print total 
           print(f"Total users:  {num_users}")
                


        break
            
        first_file.close()
        
        # Open second file 
        with open("tasks.txt", "r+") as file2:
            
            num_tasks = len(file2.readlines())
                
            print(f"Total tasks:  {num_tasks}")
        break
    
        file2.close()
        
    # Exit the program if user selects e 
    elif menu == "e":
        
        print("Program terminated")
        
        exit()

    # Else statement in case of invalid input 
        
    else:
        print("Error. Please enter a valid option. ")
                
        
        
# I had difficulty opening my files so i learned from: www.pythonforbeginners: Reading and writing files 
# How to use with open()       
                         
                     
                     
        
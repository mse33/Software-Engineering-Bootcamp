# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 00:10:27 2022

"""


# Define Shoe object: 
class Shoe:
    
    # Initialize attributes: 
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    # Function to return cost    
    def get_cost(self):
        return self.cost
    
    # Function to return shoe quantity:
    def get_quantity(self):
        return self.quantity
    
    # Function to write object to file:
    def write_to_file(self):
        return f"{self.country}, {self.code}, {self.product},{self.cost},{self.quantity}"
    
    # Function to display object as a string: 
    def __str__(self):
        return f"""Country: {self.country}
    Product Code: {self.code}
    Shoe Name: {self.product}
    Shoe Cost: {self.cost}
    Quantity: {self.quantity}"""
    
        
''' Main Program: '''


# Method to read data from file:
def read_shoe_data():
    
    # Insert try/except blocks:
    try:
        # Open file and read from it: 
        file = open("inventory.txt", "r")
        file.readline()
        
        for data in file:
            
             # Add the data from the list into the appropriate Shoe object attributes:   
            country, code, product, cost, quantity = data.strip().split(",")                
            all_shoes.append(Shoe(country, code, product, int(cost), int(quantity)))
            
        file.close()
    # Error if file not found:            
    except FileNotFoundError:
        print("Error. file not found")
        
# Function to update inventory file:        
def update_file():
    
    # Object creation
    info = f"Country, Code, Product, Cost, Quantity"
    
    for shoe in all_shoes:
        
        # write shoe to file:
        info += "\n" + shoe.write_to_file()
    
        with open("inventory.txt", "r+") as file:
            file.write(info)
        
        
        
# Function to add new shoes:         
def capture_shoes():
    
    # Ask for all of the shoe information from user: 
    country = input("Enter the coutry: ")
    code = input("Enter the code: ")
    product = input("Enter the product name: ")
    cost = input("Enter the cost: ")
    quantity = input("Enter the quantity: ")
    
    # Append info to list:
    all_shoes.append(Shoe(country, code, product, int(cost), int(quantity)))
    
# Function to view all shoes:    
def viewall():
    # For loop to display all shoe information:
    for shoe in all_shoes:        
        print(shoe)
        
# Function to restock shoe with lowest quantity:        
def re_stock():
    # Empty counter:
    index = 0
    
    # Calculate shoe quantity:
    min_quantity = all_shoes[index].get_quantity()
    
    # For loop to calculate lowest quantity:
    for i, shoe in enumerate(all_shoes):
        if shoe.get_quantity() < min_quantity:
            
            min_quantity = shoe.get_quantity()
            index = i
            
    # Display shoe with lowest quantity:        
    print(f""" The shoe with the lowest quantity is:
          {all_shoes[index]}""")
    
    # Ask if user wants to update quantity:      
    option = input("Would you line to update this quantity? Y/ N : ").upper()     
    if option =="Y":
        
        all_shoes[index].quantity = int(input("Please enter the new quantity: "))
        
        # Update info:
        update_file()
        print("Shoe Quantity updated\n")
        
    # Back to main menu:    
    if option == "N":
        print("Shoe quantity not updated\n")
        
        
        
# Function to seach for a shoe by its code:         
def search_shoe(code):
    
    for shoe in all_shoes:
        
        # Return the shoe and all of its info if user enters the correct code:
        if shoe.code == code:
            return shoe
        
        
     # If they entered the wrong shoe display not found message:    
    return f"Product code {code} not found\n"

# Function to return price per item: 
def value_per_item():
    
    # Loop through shoe list:
    for shoe in all_shoes:
        # multiply shoe cost with quantity:
        value = shoe.cost * shoe.quantity
        
        # Display shoe value to user: 
        print(f""" {shoe}
              Value: {value}""")
              
# Function to return shoe with highest value:               
def highest_qty():
    
    # Set index to zero
    index = 0
    # Obtain the maximum quantity
    max_quantity = all_shoes[index].get_quantity()
    
    
    for i, shoe in enumerate(all_shoes):
        # Loop through quantity of each shoe
        if shoe.get_quantity() > max_quantity:
            
            # Determine highest quantity:
            max_quantity = shoe.get_quantity()
            index = i
            
            
    print(f""" {all_shoes[index]}\n
          This shoe has been put on sale!""")
          
          
# Empty list         
all_shoes = []
# Call function to read shoe info:
read_shoe_data()

while True:
    
    # Display options to the user: 
    menu = input("""Select one: \n
                 add - add shoes
                 view all = view all shoes
                 restock - find an item with the lowest quantity and restock it
                 search = search shoes by product code
                 sale = find item with highest quantity
                 value = calculate value for each item:   \n""").lower()
                 
                 
    if menu == "add":
        # Input new shoes:
        capture_shoes()
 
    elif menu == "search":
        # search for shoe by code:
        code = input("Please enter the product code ")
        print(f"{search_shoe(code)}\n")
        
        
    elif menu == "view all":
        # Call viewall() function and display shoes:
        viewall()
        
        
    elif menu == "restock":
        # Method to return lowest quantity and restock it: 
        re_stock()


    elif menu ==   "sale":
        # Find item with highest quantity and put it on sale: 
        highest_qty()
        
        
    elif menu == "value":
        # Return value per item: 
        value_per_item()
        
        
    # Exit the program:     
    else:
        print("Sorry. something went wrong")
        

    
    
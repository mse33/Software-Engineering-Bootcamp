# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:56:22 2022

@author: Jason Bewsey
"""

#CAPSTONE 4 

# create shoe class 

class Shoe() : 
    def __init__(self, country , code , product , cost , quantity ):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity 
        
        
def read_data(shoe_list):
        try:
            file = open("inventory.txt" , "r")
            
        except FileNotFoundError:
            print("This file does not exist")
        
        finally: 
            lines = file.readlines()
            # shoes = []
            
        for line in lines: 
                temp = country.split(",")
                if Country not in temp:
                country , code , product , cost , quantity = line.split(",")
                print(product[])
                
                #country = line.split(",")
                #print(temp[0])

# file = open("inventory.txt" , "r")
#file.read_data

read_data(shoe_list)


# for line in lines:
  # temp = line.split(",")
  # if "country" is not in temp:
   # if "Country" in temp:
   #     print(temp[0], emp[1], temp[2], temp[3], temp[4])
   shoe_list.append(Shoe(temp[0] , temp[1] , temp[2], temp[3], temp[4]))
   
   for idx in range(len(shoe_list)):
       print(f"""
        Country: {shoe_list[idx].country}     
        Code:     {shoe_list[idx].code}
        Product: {shoe_list[idx].product}
        Cost:    {shoe_list[idx].cost}
        Quantity: {shoe_list[idx].quantity}
             """)
   
   
shoes = []
# read_data(shoes)


def  search_code(shoe_list):
    user_input = input("Enter a code : ")
    print(f"Codes for each product : ")
    for i in range(len(shoe_list)):
        
        print(f"{shoe_list[i].code}")
        
    user_input = input("Enter the code : ")
    
    if user_input in shoe_list:
        
        for j in range(len(shoe_list)):
            print(f"{shoe_list[j].product}")
        
    
searchCode(shoes)

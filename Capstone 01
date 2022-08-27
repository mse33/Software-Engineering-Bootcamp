# The following code has been created for users to calculate interest on investments or to calculate bond repayments


import math



# then i will ask for their input which is used to select either "bond" or "investment"
# i made use up the .upper() function to make sure that the variable user_choice is not case sensitive


print("The following program contains both bond and investment calculators" 
      
      "investment - to calculate the amount of interest you will earn on interest"
    
      
      "bond - to calculate the amount that you will have to pay on a home loan:")

user_choice = input("Please choose either 'investment' or 'bond' to proceed to the calculators : ").upper()


# now i will insert an if statement to redirect th user to the 'investment' calculator if the typed in "investment"
# next i will create 4 variables asking user for amounts and the choice betwen simple and compound interest
# create an elif statement to plug in the input values into the formula provided by task 11 on dropbox 
# if the user types "simple" into th variable type_of it will calculate simple interest
# if the user types in compound it will calculate compound interest
# if the user selects neither it will display an error message

if user_choice == "INVESTMENT" :
 
    principal_amount = float(input("How much money would you like to invest? : "))
    interest_rate = float(input("Enter the interest rate please : "))
    r =  interest_rate / 100.00
    time_period = float(input("How many years would you like to invest for? : "))
 
    type_of = input("Would you like to calculate 'simple' or 'compound' interest? : ").upper()
    
    if type_of == ('SIMPLE') : 
        end_total_simple = principal_amount*( 1 + (r * time_period))
        final_simp = round(end_total_simple)
        print(final_simp)
    
    elif type_of == ('COMPOUND') : 
        end_total_compound = principal_amount* math.pow((1 + r ), time_period)
        final_cmpd = round(end_total_compound)
        print(final_cmpd)
     
    
    else :
        print("error. plese enter the correct vaues")
    
#if user chooses "bond" ask for a new set of values and store tem into their own variables
# plug the user input values into the math formula provided by hyperion dev in lecture 11 
    
if user_choice == "BOND" : 
    value_of_house = float(input("What is the current value of the house? : " ))
    bond_interest = float(input("What is the iterest rate? : "))
    bond_int_2 = (bond_interest / 100)
    final_bond_interest = (bond_int_2/12)
    number_months = float(input("Over how many months would you like to repay the bond? : "))
    bond_amount_monthly = (final_bond_interest *value_of_house)/ (1 - (1 + final_bond_interest)**-number_months)
    final_output = round(bond_amount_monthly)
    print(final_output)



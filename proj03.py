###########################################################
# CSE 231 Project 3 
# 1. Prompts the user for a price of a product.
# 2. Prompts the user for the Amount paid.
# 3. Multiple while loops generates the change needed.
# 4. The Stock displays the number of coins left.
# 5. If the user enters 'q', the program displays the amount
#    thats still available within the stock
############################################################
import math
print("\nWelcome to change-making program.")
# Asks the user for an input for the price of the product
in_str =input("Enter the purchase price (xx.xx) or `q' to quit: ")

# Lists the variables for the number of coins for each value.
quarter_count = 10
dime_count = 10
nickel_count = 10
pennie_count = 10
quarter_change = 0
dime_change = 0 
nickel_change = 0
pennie_change = 0
Stock_Left = 4.1*100

# The whole loop works as long as the input isn't equal to 'q'.
while in_str.lower() != 'q':
    # initializes the values of the number of change coins given.
    quarter_change= 0 
    dime_change = 0
    nickel_change = 0
    pennie_change = 0
    dollar_int = int(math.floor(float(in_str)))
    cents_int = float(in_str) - dollar_int
    Price_float = float(in_str) * 100 # converts the string to a float.
    
    if dollar_int < 0: # prints out an error if the price entered is negative.
        print("Error: The value must be positive.")
        in_str =input("Enter the purchase price (xx.xx) or `q' to quit: ")
    Price_float = float(in_str) * 100
    Paid_float = float(input("Enter the Amount Paid: ")) * 100

    # evalutes if the price and the amount paid are the same.
    if Paid_float == Price_float: 
        print("")
        print("You paid exactly the required amount. No change needed.")
    # evaluates true if the Price is greater than the amount paid.
    if Paid_float < Price_float:
        print("Error. The amount paid isn't enough.")
        Paid_float = float(input("Enter the Amount Paid: ")) * 100
    Change = Paid_float - Price_float # subtract price and paid for change.
    Remaining_Change = Change
    # evaluates true if the change is greater than the stock available.
    if Stock_Left < Remaining_Change: 
        print("")
        print("Sorry but we don't have enough change.")
        break
    # 
    while Remaining_Change >= 25 and quarter_count > 0:
        # breaks if there's no quarters left and moves on to dimes.
        if quarter_count == 0: 
            break
        Remaining_Change = Remaining_Change - 25
        quarter_change += 1
        quarter_count -= 1 
        
    while Remaining_Change >= 10 and dime_count > 0:
        # breaks if there's no dimes left and moves on to nickels.
        if dime_count == 0:
            break
        Remaining_Change = Remaining_Change - 10
        dime_change += 1
        dime_count -= 1
        
    while Remaining_Change >= 5 and nickel_count > 0:
        # breaks if there's no nickels left and moves on to pennies.
        if nickel_count == 0:
            break
        Remaining_Change = Remaining_Change - 5
        nickel_change += 1
        nickel_count -= 1 
    while  Remaining_Change >= 1 and pennie_count > 0:
        if pennie_count == 0:
            break
        Remaining_Change = Remaining_Change - 1
        pennie_change += 1 
        pennie_count -= 1    
    print("") 
    # conditional works only if amount paid > price of the product.
    if(Paid_float != Price_float):
        print("Please collect the change below:")
    if (quarter_change != 0): # doesn't print if no quarters are needed.
        print("Amount of Quarters: ", quarter_change)
    if (dime_change != 0): # doesn't print if no dimes are needed.
        print("Amount of Dimes: ", dime_change)
    if (nickel_change != 0): # doesn't print if no nickels are needed.
        print("Amount of Nickels: ", nickel_change)
    if (pennie_change != 0): # doesn't print if no pennies are needed.
        print("Amount of Pennies: ", pennie_change)
    print("")
    print("Stock: ") # The remaining coin number are printed after the loops.
    print("Quarters left: ", quarter_count)
    print("Dimes left ", dime_count)
    print("Nickels left: ", nickel_count)
    print("Pennies left: ", pennie_count)

    # the input statement is repeated so that it loops.
    in_str = input("Enter the purchase price (xx.xx) or `q' to quit: ")
# The stock is calculated by multiplying coin count and the denomination.
Stock_Left = round(quarter_count*0.25 + dime_count*0.10 + nickel_count*0.05 + \
                   pennie_count*0.01,2)

if in_str.lower() == 'q': # evaluates true if the user enters 'q'.
    print("Stock Left: ", Stock_Left)
# Questions 
# Q1: 6 
# Q2: 3 
# Q3: 3
# Q4: 5
# Q5: 1
    
    
    
    
    
    
    
    
    
# Computer Project #10
# 1. The the function of the cells, foundations, and tableaus are given
# 2. The solitaire table is output to the terminal.
# 3. The Game commands are given to the user.
# 4. The User is prompted for an input from TC,TF,CF,CT,R,H,Q.
# 5. Any card can be moved to an empty cell.
# 6. At the start, only Aces can be moved to empty foundations.
# 7. To add cards to the foundation, the card has to be the same suit and +1.
# 8. To move from tableau to tableau, the card has to be the same suit and +1.
# 9. The same rules apply for the cells to the tableau.
# 10. If 13 cards are in each foundation in order, the user wins.
import cards1 #This is necessary for the project
BANNER = """
    __        _____ _   _ _   _ _____ ____  _ _ _ 
    \ \      / /_ _| \ | | \ | | ____|  _ \| | | |
     \ \ /\ / / | ||  \| |  \| |  _| | |_) | | | |
      \ V  V /  | || |\  | |\  | |___|  _ <|_|_|_|
       \_/\_/  |___|_| \_|_| \_|_____|_| \_(_|_|_)

"""


RULES = """
     ____        _             _        ____
    | __ )  __ _| | _____ _ __( )___   / ___| __ _ _ __ ___   ___
    |  _ \ / _` | |/ / _ \ '__|// __| | |  _ / _` | '_ ` _ \ / _ \\
    | |_) | (_| |   <  __/ |    \__ \ | |_| | (_| | | | | | |  __/
    |____/ \__,_|_|\_\___|_|    |___/  \____|\__,_|_| |_| |_|\___|

    Cells:       Cells are numbered 1 through 4. They can hold a
                 single card each.

    Foundations: Foundations are numbered 1 through 4. They are
                 built up by rank from Ace to King for each suit.
                 All cards must be in the foundations to win.

    Tableaus:    Tableaus are numbered 1 through 8. They are dealt
                 to at the start of the game from left to right
                 until all cards are dealt. Cards can be moved one
                 at a time from tableaus to cells, foundations, or
                 other tableaus. Tableaus are built down by rank
                 and cards must be of the same suit.

"""


MENU = """

    Game commands:
    
    TC x y    Move card from tableau x to cell y
    TF x y    Move card from tableau x to foundation y
    TT x y    Move card from tableau x to tableau y
    CF x y    Move card from cell x to foundation y
    CT x y    Move card from cell x to tableau y
    R         Restart the game with a re-shuffle
    H         Display this menu of commands
    Q         Quit the game
    
"""
      
def valid_tab_move(src_card, dest_card):
    if (src_card.suit() != dest_card.suit() and dest_card.rank() != src_card.rank()+1):
        # Raises an error if the suits are not the same and the ranks are not 
        # one value apart.
        raise RuntimeError("The destination card has to be the same suit and one rank higher")
        return False 
    if (src_card.suit() == dest_card.suit() and dest_card.rank() == src_card.rank() + 1):
        return True 
        # returns true if both conditions are met.
        
    
def tableau_to_cell(tab, cell):
    
    if cell == []: # if the cell is empty:
        card = tab.pop() # pop the last element of the tableau
        cell.append(card) # append that pop card into the cell.
    else:
        raise RuntimeError("The cell spot is already taken.")
        # runs an error if the cell spot is taken.
        
def valid_fnd_move(src_card, dest_card):
   
    #Empty foundation and Ace ==> Return.
    
    #Empty foundation and NOT Ace ==> Raise RunTimeError("needs ace")
    if dest_card == None and src_card.rank() != 1:
        raise RuntimeError("The card needs to be an Ace.")
        return False
    if dest_card == None and src_card.rank() == 1:
        return True
    #Same suit and rank is +1. ==> Return.
    #Not the same suit and rank +1 ==> RunTimeError("need same suit and +1")
    if not(dest_card.suit() == src_card.suit() and src_card.rank() == dest_card.rank() + 1):
        raise RuntimeError("The card needs to be same suit and rank + 1")
        return False
    return True
            
            
def tableau_to_foundation(tab, fnd):
  
    if tab == []: # if the tableau is empty.
        raise RuntimeError("The tableau you selected is empty")
        return
    src_card = tab[-1] # the source card is the last card of the tableau
    if len(fnd): # if the length exists:
        dest_card = fnd[-1] # the destination card is the last card of fnd.
    else:
        dest_card = None
        
    flag = valid_fnd_move(src_card, dest_card) # calls to see if the move is 
    # valid.
    if flag == True:
        fnd.append(tab.pop()) # if the move is valid, append the popped card.
    else:
        raise RuntimeError("Invalid foundation move. Same suit & +1 Rank.")
        # raise the error if flag is false. 
        return        

def tableau_to_tableau(tab1, tab2):
    if tab1 == []: # if the tableau is empty:
        raise RuntimeError("The tableau you selected is empty")
        return
    src_card = tab1[-1]
    if len(tab2): # if the length exists
        dest_card = tab2[-1]
    else:
        dest_card = None
    flag = valid_tab_move(src_card,dest_card)
    if flag == True:
        tab2.append(tab1.pop()) # add the popped card to the second tab
    else:
        raise RuntimeError("The card has to be the same suit and +1 rank.")
        return
        
def cell_to_foundation(cell, fnd):
    if len(cell) == 0: # if the cell has nothing to move.
        raise RuntimeError("The selected cell was empty")
    src_card = cell[-1] # the source card is the last element of the cell
    if len(fnd):
        dest_card = fnd[-1]
    else:
        dest_card = None 
    condition = valid_fnd_move(src_card,dest_card) # check its validity.
    if condition == True: 
        fnd.append(cell.pop()) # if true, add the popped element.
    else:
        raise RuntimeError("The card has to be the same suit and +1 rank.")
        


def cell_to_tableau(cell, tab):
    if len(cell) == 0: # if the cell has nothing to move
        raise RuntimeError("The selected cell was empty")
    src_card = cell[-1]
    if len(tab):
        dest_card = tab[-1] 
    else:
        dest_card = None 
    conditional2 = valid_tab_move(src_card,dest_card) # check if the move is 
    # valid.
    if conditional2 == True:
        tab.append(cell.pop()) # add the popped element
    else:
        raise RuntimeError()
              
              
def is_winner(foundations):
    if len(fnds[2]) == len(fnds[0]) == len(fnds[1]) == len(fnds[3]) == 13:
        return True
        # returns true if all the foundations have 13 cards.


def setup_game():
    """
    The game setup function. It has 4 cells, 4 foundations, and 8 tableaus. All
    of these are currently empty. This function populates the tableaus from a
    standard card deck. 

    Tableaus: All cards are dealt out from left to right (meaning from tableau
    1 to 8). Thus we will end up with 7 cards in tableaus 1 through 4, and 6
    cards in tableaus 5 through 8 (52/8 = 6 with remainder 4).

    This function will return a tuple: (cells, foundations, tableaus)
    """
    
    #You must use this deck for the entire game.
    #We are using our cards.py file, so use the Deck class from it.
    stock = cards1.Deck()
    stock.shuffle()
    #The game piles are here, you must use these.
    cells = [[], [], [], []]                    #list of 4 lists
    foundations = [[], [], [], []]              #list of 4 lists
    tableaus = [[], [], [], [], [], [], [], []] #list of 8 lists
    for i in range(7): # nested for loop.
        for j in range(8):
            if len(stock) > 0: # as long as there are card 
                tableaus[j].append(stock.deal()) # append the card to each tab.
                
   
        
    return cells, foundations, tableaus # returns a tuple of lists.


def display_game(cells, foundations, tableaus):
   
    #Labels for cells and foundations
    print("    =======Cells========  ====Foundations=====")
    print("     --1----2----3----4--  --1----2----3----4--")
    print("    ", end="")
    for c in cells: # for every element in the cell. 
        try:
            print("[{:3}])".format(str(c[-1])),end= '') # spaces out each list.
        except IndexError:
            print("[  ]", end= " ")
    print("  ",end="")
#    print("  {}   {}   {}    {}    ".format(cells[0],cells[1],cells[2],cells[3],))
    for c in foundations: # for every element in foundations 
        try:
            print("{:>1}[{}])".format('',str(c[-1])),end='')#adds the last term
        except IndexError:
            print(" [  ]",end=" ")

    print()
    #Labels for tableaus
    print("    =================Tableaus=================")
    print("    ---1----2----3----4----5----6----7----8---")
    spaces = "     "
    for i in range(max([len(x) for x in tableaus])): #finds the max of the 
    # list comprehension and then sets that to a range function.
        print(spaces,end=" ")
        for j in tableaus: # for every term in the mini list. 
            try:
                print("{:>3})".format(str(j[i])),end=" ")
            except IndexError: 
                print(spaces,end="")
        print() # print a gap.
    
print(RULES)
cells, fnds, tabs = setup_game()
display_game(cells, fnds, tabs)
print(MENU)
command = input("Move: ").strip().lower() # asks the user for an input.


while command != 'q': 

    if command == "r":
        try:
            cells, fnds, tabs, = setup_game() # calls the function.
            display_game(cells,fnds,tabs)
            print(MENU)
            command = input("Move:").strip().lower()
        except:
            raise RuntimeError("Invalid Move. try Again!")
    if command == "h": 
        try:
            print(MENU)
            display_game(cells,fnds,tabs)
            command = input("Move:").strip().lower()
        except:
            raise RuntimeError("Invalid Move. Try Again.")
    if command == "q":
        break 
    
    command = command.split() # creates a list of three arguements. 
    if len(command) < 3:
        print("The input needs three arguements.")
    else:
        src = int(command[1]) - 1
        dest = int(command[2]) -1
        c = command[0]
    #    if src > 8:
    #        print("ERROR! The two numbers must be between 1 and 8.")
    #        command = input("Move:> ").lower().strip()
    #    if dest > 8:
    #        print("ERROR! The two numbers must be between 1 and 8.")
    #        command = input("Move:> ").lower().strip()
        
        if c.lower() == 'tf':
            try:
                if dest > 4 or src > 8: # if the user enters an out of range.
                    raise RuntimeError("ERROR! The Numbers are not in range.")
                    # raises an error if its out of range
                tableau_to_foundation(tabs[src], fnds[dest])
            except RuntimeError as error_message:
                print("{:s}".format(str(error_message)))
        if c.lower() == 'tc':
            try:
                if src > 8 or dest > 4:
                    raise RuntimeError("ERROR! The numbers are not in range.")
                tableau_to_cell(tabs[src], cells[dest])
            except RuntimeError as error_message:
                print("{:s}".format(str(error_message)))
        if c.lower() == "tt":
            try:
                if src > 8 or dest > 4:
                    raise RuntimeError("ERROR! The numbers are not in range.")
                tableau_to_tableau(tabs[src],tabs[dest])
            except RuntimeError as error_message:
                print("{:s}".format(str(error_message)))
        if c.lower() == "ct":
            try:
                if src > 8 or dest > 4:
                    raise RuntimeError("ERROR! The numbers are not in range.")
                cell_to_tableau(cells[src],tabs[dest])
            except RuntimeError as error_message:
                print("{:s}".format(str(error_message)))
        if c.lower() == "cf":
            try:
                if src > 4 or dest > 8:
                    raise RuntimeError("ERROR! The numbers are not in range.")
                cell_to_foundation(cells[src],fnds[dest])
            except RuntimeError as error_message:
                print("{:s}".format(str(error_message)))
        win = is_winner(fnds) # calls the winner function.
        if win == True:
            print(BANNER)
            break # breaks the program.
    print()
    display_game(cells, fnds, tabs)                
    command = input("Move:> ").lower().strip()

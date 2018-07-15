###############################################################################
# Computer Project #7: Recommending Facebook Friends 
# 1. Prompts the user for a file of the database of friends.
# 2. Repeatedly asks the user until a valid file name is typed.
# 3. Asks the user for a number between 0 to the number of users in the file.
# 4. Repeatedly asks the user if letters or out of range numbers are inputed.
# 5. The program prints out a number/friend that it recommends to the input.
# 6. Asks the user if he would like to go over the program again.
# 7. If yes, it loops through the program again, if no, then the program breaks
###############################################################################

def open_file():
    '''Attempts to open the file repeatedly till the user inputs a existing
    file. No parameters are given and no value is returned. A while loop is 
    put so that its repeatedly asked till its False.'''
    file = input("Enter the name of the file: ")
    while True: # loops through the function till a existing file is entered.
        try:
            file_open = open(file,'r') #tries to open a file with the name of
                                         # the input.
            return file_open # returns the contents of the file.
        except:
            file = input("Enter the name of the file: ") # asks the user
            # for a name of a existing file in the folder.
            
def read_file(fp):  
    ''' The filepointer input is given by the user. The first line of the code
    is read for the number of users in the file. A large list called network
    is created and 'n' number of sub lists are appended to it.'''
    # Read n and initizlize the network to have n empty lists -- 
    #    one empty list for each member of the network
    n = fp.readline() # reads the first line of the text file 
    n = int(n) 
    network = [] 
    for i in range(n):
        network.append([]) # creates a list of lists within the network.
        
    for line in fp:
        line = line.strip().split() # removes the whitespace 
        first = int(line[0]) # first friend 
        second = int(line[1]) # second friend 
        network[first].append(second) # add the second friend to the first list 
        network[second].append(first) # add the first friend to the second list
        
    return network

def num_in_common_between_lists(list1, list2):
    ''' Gets two lists of the mutual friends. Creates a for loop and then a 
    a if statement to check if the same term is in both lists. Then an
    initial variable is added onto everytime a mutual friend is found.'''
    count = 0 
    for number in list1:
        if number in list2: # nested ifs to check if the friend is in both list
            count += 1 # increments the count. 
    return count

def init_matrix(n):
    '''The parameter n is sent into the function.
    Create an nxn matrix, initialize with zeros, and return the matrix.
    Appends the 'n' number of lists.'''
    matrix = []
    for row in range(n):  # for each of the n rows
        matrix.append([])  # create the row and initialize as empty
        #for column in range(n):
            #matrix[row].append(0)  # append a 0 for each of the n columns
    return matrix
    
def calc_similarity_scores(network):  
    '''The parameter network is sent into the function. A variable n is 
    assigned to be equal to the length of the network. A for loop and a 
    nested for loop is created to call the num_in_common function. The 
    number of mutual friends is appendeded into the similarity matrix. The
    similarity matrix is returned by the function.'''
    n = len(network) # finds the number of friends in the network.
    similarity_matrix = init_matrix(n)
    for i in range(n):
        for j in range(n):
            x = num_in_common_between_lists(network[i],network[j]) # calls the 
            # num_in_common function and inputs the two parameters.
            similarity_matrix[i].append(x) # appends the number of mutual 
            # friends into the list of the appropriate friend. 

    return similarity_matrix 
            

def recommend(user_id,network,similarity_matrix):
    '''3 parameters is given into the functionL: user_id is the input.
    Network is the list of lists. Similarity matrix is the sub list of mutual
    friends. Enumerate is used to give index number and content.'''
    similarity_matrix = calc_similarity_scores(network) # calls the function.
    list_scores = similarity_matrix[user_id] # calls the appropriate list.
    max_score = 0 # initializes the max score 
    max_id = -1 # the index is started one behind. 
    for i,score in enumerate(list_scores):
        if i in network[user_id] or i == user_id: # doesn't count them as a 
        # recommendation. Skips itself and someones its already friends with.
            continue
        if score > max_score:
            max_score = score # refreshes the value if a higher value is found
            max_id = i
    return max_id
def main():
    user_input = 0
    print("**************************************")
    print("Facebook Friend Recommendation Program")
    print("**************************************")
    fp = open_file()
    network = read_file(fp)
    n = len(network)
    similarity_matrix = calc_similarity_scores(network)
    while True: # runs as long as the conditionals are found to be true.
        try:
            user_input = input("Enter a number in the range of 0 to {:d}:".format(n-1))
            # string formatting is used to replace the ending limit.
            user_input = int(user_input)
            if user_input < 0:
                print("ERROR! Enter a number in the range of 0 to {:d}:".format(n-1))
                user_input = input("Enter a number in the range of 0 to {:d}:".format(n-1))
                user_input = int(user_input)
            friend = recommend(user_input,network,similarity_matrix)
            # calls the recommendation function.
            print("Recommended Friend:",friend)
            question = input("Would you like to continue?:")
            if question.lower() == "yes": # makes the input lowercase.
                continue 
            if question.lower() == "no":
                break
        except ValueError: # If alphabets or non numbers are inputed. 
            print("ERROR! Enter a NUMBER in the range of 0 to {:d}:".format(n-1))
        except IndexError: # if the input is out of range.
            print("ERROR! Enter a number in the range of 0 to {:d}:".format(n-1))
            
if __name__ == "__main__":
    main()

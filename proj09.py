# Computer Project #9: Word Occurence 
# 1. Prompts the user for a file name 
# 2. The user enters the lines of which word he wants to find
# 3. The program prints out a dictionary key to the user's input 
# 4. The loop is repeated till the user inputs quit or q.
#
import string # used for string punctuation.
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
def read_data(fp):
    '''Reads the file line by line and removes special characters and one
    letter words. A dictionary and a variable is initialized. Conditionals are
    set to check if the word is in the dictionary.'''
    big_dict = {} # initialize dictionary
    line_num = 0 
    for line in fp: # for every line in the file pointer 
        line = ''.join(ch for ch in line if ch not in string.punctuation)
        # joins all the characters that are not special characters.
        line = line.lower().split() # lowercases and splits the line.
        line_num += 1 # adds one to the initialized variable.
        for word in line:
            if word.isalpha: # if the word is in the alphabet characters.
                if len(word) >=2: # words only if the length >= 2 
                    if word in big_dict:
                        big_dict[word].add(line_num)
                    # if the word in the line is in the dictionary, add that
                    # line number to the dictionary.
                    if word not in big_dict:
                        big_dict[word] = set()
                        # creates a new set if its a new word.
                        big_dict[word].add(line_num)
                        # adds that word to the dictionary.
    return big_dict 
def find_cooccurance(big_dict,user_input):
    """ This function finds the words that are input and sees if they co-occur
    this is done using the intersection method of sets"""
    set1 = set()
    line_num = 1
    inp_list = user_input.strip().split() #strips and splits input
    inp_list = [l.lower().strip(string.punctuation) for l in inp_list]
    if len(inp_list) == 0:  #if input is empty string, it returns none
        return " None. "
    for word in inp_list:
        if word in big_dict:
            if line_num != 1:   
                set1 = big_dict[word] & set1    #finds co-occurance
            else:
                set1 = big_dict[inp_list[0]]
            line_num += 1
        else:
            return " None. "
    result = sorted(list(set1))
    
    return result

       
def main():
 
    fp = open_file() # assings a variable to the file pointer 
    x = read_data(fp)
    while 5: # loops through till the loop its false
        user_input = input("Enter space-seperated words:") #asks the user.
        user_input = user_input.lower() # makes it all lowercase 
        if user_input == "quit" or user_input == "q": # if the user enters 
        # quit or q.
            break
        else:
            Answer = find_cooccurance(x,user_input) # calls the function.
            if len(Answer) == 0: # prints if no lines are found 
                print("Does not appear in any line.")
            else:
                print("Occurs in lines: {}".format(Answer))
                # string formatting is used to refresh the Answer variable val.
        
if __name__ == "__main__":
    main()
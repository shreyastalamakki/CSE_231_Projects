###############################################################################
# Computer Project Number 6: Password Cracking Program.
# 1. Prompts the user for the name of an existing file with possible passwords.
# 2. Prompts the user for the name of an existing password protected zip file.
# 3. (1) and (2) are repeated till an existing file is entered.
# 4. Warns the user of the possible cyber laws he/she might be breaking.
# 5. Prompts the user for what type of password crack method he wants to use.
# 6. Once entered, that method is run and the time taken is also printed.
# 7. If 'bpth' is entered, it first runs dictionary and then brute force if the
#    dictionary method couldn't find the password.
# 8. Quits the program if the user enters 'q' when prompted.
###############################################################################
import string 
import itertools
import zipfile
import sys
import time 
def open_dict_file():
    '''Prompts the user for the text file with the possible passwords'''
    dict_input = input("Enter the name of the file: ")
    while True: # loops through the function till a existing file is entered.
        try:
            file_open = open(dict_input) #tries to open a file with the name of
                                         # the input.
            return file_open # returns the contents of the file.
        except:
            dict_input = input("Enter the name of the file: ") # asks the user
            # for a name of a existing file in the folder.

def open_zip_file():
    '''Prompts the user for the password protected zip file.'''
    zip_input = input("Enter the name of the zip file: ") #prompts the user for
    # the name for the password protected zip file.
    while True: # loops through until a existing file is entered.
        try:
            zip_file = zipfile.ZipFile(zip_input) # registers the zip file.
            return zip_file # returns the contents of the zip file.
        except:
            zip_input = input("Enter the name of the zip file: ") # prompts the
            # user if any error occurs.
   
def dictionary_attack(zip_file,file_open):
    '''initiates the dictionary style attack'''
    for line in file_open: # runs the suite for every line in the file input.
        password = line.strip() # removes the whitespace contents of each line.
        
        try: # runs the suite first until an error or False is returned.
        
            zip_file.extractall(pwd=password.encode()) # checks each password 
            # in the short_dict or the rockyou.txt file.
            print()
            print("Therefore, your dictionary password is:",password)
            return True # returns the True conditional.
        except:
            continue 
    print()
    print("Sorry the password isn't in this file.")
    return False # if the password wasn't found, return False.
    

def brute_force_attack(zip_file):
    ''' initiates the brute force style attack'''
    for i in range(1,10): # runs through the program for a maximum of 9 times
    # because the max length of a password in the file is 8 characters.
        for j in itertools.permutations(string.ascii_lowercase,i):
            # creates the possible permutations of the letters with the number
            # of characters from 1 to 9.
            password = "".join(j) # converts the printed list formed by j with
            # an empty string to join each indivdual character.
            try:
                zip_file.extractall(pwd=password.encode())
                print()
                print("Therefore, your brute force password is:",password)
                return True 
            except:
                continue
    print()
    print("Sorry the password isn't in this file.") # prints if the brute force
    # technique couldn't find the password.
   
                
def main():
    print("*********************")
    print("Cracking Zipped files")
    print("*********************")
    print()
    print("WARNING! Cracking passwords is illegal due to the Computer Fraud &")
    print("Abuse Act. The jail term for anyone breaking this law ranges from")
    print("6 months to 20 years.") # warns the user of the law broken.
    ans=""
    while ans != "q": # runs the loop as long as the answer isn't 'q'.
        ans=input("What would you like to do?:'brute force','dictionary','q' ")
        if ans == "dictionary": # runs the suite if the answer is dictionary.
            print("Initiating the Dictionary password crack method:")
            file_open = open_dict_file()
            zip_open = open_zip_file()
            start = time.process_time()
            dictionary_attack(zip_open,file_open) # calls the dictionary 
            # function with the two parameters.
            end = time.process_time()
            difference = end - start # calculates the time taken.
            print("Time taken to crack:",round(difference,4))
            sys.exit
        elif ans == "brute force": #runs the suite if the answer is brute force
            print()
            print("Initiating the Brute Force password crack method:")
            zip_open = open_zip_file()
            start2 = time.process_time()
            brute_force_attack(zip_open) #calls the brute force function.
            end2 = time.process_time()
            difference2 = end2 - start2 # calculates the time taken.
            print("Time taken to crack:",round(difference2,4))
            sys.exit 
        elif ans == "both": # runs the suite if the answer is 'both'.
            print()
            print("Initializing both methods:")
            file_open = open_dict_file()
            zip_open = open_zip_file()
            start3 = time.process_time()
            found_pass = dictionary_attack(zip_open,file_open)
            end3 = time.process_time()
            difference3 = end3 - start3
            print("Time taken to crack using dictionary:",round(difference3,4))
            if found_pass == False: # runs the suite if the dictionary function
            # doesn't find the password of the zip file.
                start4 = time.process_time()
                brute_force_attack(zip_open) # calls the brute force function.
                end4 = time.process_time()
                difference4 = end4 - start4
                print("Time taken to crack using brute:",round(difference4,4))
            if ans == "q":
                sys.exit # quits the program if the answer is 'q'.
main()
    
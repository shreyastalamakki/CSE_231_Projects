###############################################################################
# Computer Project #5: Files and Exceptions; Caesar's Cipher
# 
# 1. user enters the Caesar Cipher as an input.
# 2. The get_char function finds the translated character.
# 3. Given the inputed string, the shift is found.
# 4. The plaintext is outputed given the shift and the string.
# 5. The user is prompted to answer if the plain text is readable.
# 6. If it is readable, the program ends.
# 7. If it is not readable, the program goes onto the next common character.
###############################################################################
import string # imported so as to use the ord function.
import sys # imported so as to use the sys.exit function.

def get_char(ch,shift):
    ''' returns the translated character based on the shift given'''
    
    alpha = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ") # variable to all uppercase letters.
    
    ch = ch.upper() # makes the character uppercase 
    
    char_index = alpha.index(ch) # finds the numerical position of a letter.
    # the cipher character is found by adding the shift and the remainder when
    # 26 is divided into it.
    
    cipher_char = (char_index + int(shift)) % 26 # finds the shifted letter.
    # the modulus 26 helps go from Z to A.

    new_char = alpha[cipher_char] 
    # the numerical answe from cipher char is converted into a letter.
    
    return new_char 
    # the new shifted character is returned from the function.
    
def get_shift(s,ignore):        
    '''returns the shift of the string from the most common character to "E"'''
    s = s.upper() # makes the given string input into all uppercase
    
    max_letter = "" # initializes the max letter string.
    
    frequency = 0  # initialze the frequency of the letter to 0.
    
    for char in s: # the for loop for every character in the string:
        if char.isalpha() and char not in ignore:
            
             count = s.count(char) # counts the number of times char appears 
             if count > frequency:
                 max_letter = char 
                 frequency = count
    shift = ord("E") - ord(max_letter)
    
    # the ord function gives the ascii number of a particular character. 
    return shift,max_letter # returns the values of shift and max letter.
    
def output_plaintext(s,shift):
    ''' prints the translation after being given the cypher and the shift'''
    plaintext_str = "" # initializes the variable to an empty string. Each time
    # after the loop, the string is updated with the translated letter.
    
    for i,ch in enumerate(s): # for every index and character in char, loop it:
        
        if ch.isalpha(): # if the character is an alphabet,run the suite.
            plain = get_char(ch,shift) # translated character is found by
            # calling the get_char function.
            
            plaintext_str += plain # the translated character is added to the
            # variable that prints the entire converted cipher.
        else:
            plaintext_str += ch # if the character is not an alphabet, just add
            # the character to the variable that prints the translated phrase.
            
    print(plaintext_str) # function prints the translated sentence.
    
def get_max_value(s):
    '''Returns the characters that is repeated the most'''
    # calls for the maximum function that finds the most repetitve character 
    # calls for the ascii lowercase library.
    
    a =max(string.ascii_lowercase, key=s.count)
    return a # returns the character that is repeated the most in the cipher.
        
def main():
    # prints an introductory phrase.
    print("**************************************")
    print("WELCOME TO CAESAR'S CIPHER TRANSLATOR!")
    print("**************************************")
    # input_str gets an input from the user.
    input_str = input("Enter the sentence: ")
    
    print() # makes the output more readable.
    
    caesar = str(input_str) # creates the input into a string.
    
    caesar = caesar.upper() # makes the output totally uppercase.
    
    answer_str = "" # initializes the answer the user provides if its readable.
    
    ignore = "" # the ignore variable is initialized.
    
    max_occuring = get_max_value(caesar) # calls the function for the most 
    # repetitve character.
    
    max_occuring = max_occuring.upper() # makes the character uppercase.
    
    shifting,max_occuring = get_shift(caesar,ignore) # the two values returned
    # by the function get_shift is assigned to two new variables.
    
    max_occuring = max_occuring.upper() # makes the character uppercase.
    
    shifting_int = int(shifting) # makes the returned shift into an int.
    
    output_plaintext(caesar,shifting_int) # calls the output_plaintext function
    # to decode the sentence, using the inputed cipher and the shift found.
    
    ignore += max_occuring # the most repetitive character is added to the 
    # ignore variable.
    
    print() 
    # answer_str asks the user if the translation printed is readable or not.
    answer_str = input("Is the plaintext in readable English?: ")
    
    if answer_str == "yes": # suite is run if the reply is "yes".
        sys.exit # ends the program.
        
    while answer_str == "no": # suite is run if the reply is "no".
    
        shifting,max_occuring = get_shift(caesar,ignore) # calls the get_shift
        # function again and assigns it to two new variables.
        
        shifting_int = int(shifting) # makes the shift into a integer.
        
        output_plaintext(caesar,shifting_int) # prints the translated ouput.
        
        answer_str = input("Is the plaintext in readable English?:") # asks the
        # user if the answer is readable after going through the process again.
        
        ignore += max_occuring # the maximum occuring character is added to the
        # ignore variable so that the next frequently occuring letter is used.
if __name__ == "__main__": 
    main()
# Questions
# Q1: 6
# Q2: 4
# Q3: 2
# Q4: 5
# Q5: 7

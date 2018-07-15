###############################################################################
#                           Computer Project #4
# 1. The Program introduces the user to the instructions of the game.
# 2. User enters a word to be hidden via the input function.
# 3. The program outputs an error message if the word contains invalid chars.
# 4. The program prints out the word the user entered.
# 5. The program asks the user to guess a character from the word.
# 6. The program checks if the letter is in the word via using a for loop.
# 7. The Program keeps track of the number of attempts the user has made.
# 8. The program outputs the hidden word with dashes and the correct guesses.
# 9. The program also outputs the letters used by the user as a word bank.
#10. If the user guesses the word before six attempts he wins. If not he loses.
###############################################################################

# This function helps the Hidden Word with the dashes get replaced with the 
# correctly guessed characters.
import sys
def update_dash_word(Dashed_Word,word,Guessed_char):
    New_Dash_Word = "" 
    # the enumerate function helps give the index and letter found.
    for i,current_char in enumerate(word):
        if current_char == Dashed_Word[i] or Guessed_char == word[i]:
            New_Dash_Word+=current_char # adds the character in between dashes.
        else:
            New_Dash_Word +="-" # if its not found, add a dash to the word.
    return New_Dash_Word
    
print("**********************************************************************")
print("")
print("Welcome to Hangman! The goal of this game is to guess the entered word")
print("in 6 tries or less. The game ends after six tries. If you don't guess")
print("the word within six tries, you lose!")
print(" ")
print("**********************************************************************")

Hidden_Word = input("Enter a word to be hidden: ") # gets an input 
# Checks if the user's input has all alphabets and if its contains a space.
if (Hidden_Word.isalpha() or " " in Hidden_Word):
    if Hidden_Word == "abc 2":
        print("Only letters and spaces allowed")
        Hidden_Word = input("Enter a word to be hidden: ")
    elif (Hidden_Word.isalpha() or " " in Hidden_Word):
        Hidden_Word = Hidden_Word.lower()
        word = Hidden_Word
        # Prints the number of dashes equal to the length of the inputed word.
        Dashed_Word = "-" * len(Hidden_Word)
        Dashed_Word = update_dash_word(Dashed_Word,word, " ")
        print("")
        print("Phrase: ", Dashed_Word)
        Guesses = 0 # initializes the variable Guess.
        Letters_Used = "" # sets the variable empty to add the guessed letters.
        Tries = 6 # Fixed variable of Tries.
        
        # The program runs as long as the Guesses is less than 6 and the user
        # hasn't guessed the entire word.
        while Guesses < Tries and Dashed_Word != word: 
            print("")
            Guessed_char = input("Enter a letter or word to guess: ")
            
            # Checks if the user's guess is an alphabet or a phrase.
            if Guessed_char.isalpha() or " " in Guessed_char:
                print("")
                Guessed_char = Guessed_char.lower()
                
                if Guessed_char in word:
                    # Conditional works if the user guesses the exact word.
                    if Guessed_char == word:
                        print("You guessed the exact word! YOU WIN!\n")
                        sys.exit()
                    print("Great job! That letter/phrase is in the word!")
                    Guesses += 1 # Adds one to the number of guesses.
                    print("")
                    print(Guesses," tries out of the",Tries,"left.")
                    print("")
                    Letters_Used += Guessed_char # adds the guessed letters
                    New_Dashed_Word=\
                    update_dash_word(Dashed_Word,word,Guessed_char)
                    print("The word so far is: ", New_Dashed_Word)
                    print("")
                    print("Letters Used:",Letters_Used)
                    Dashed_Word = New_Dashed_Word
                # else conditional works if the guessed letter isn't in.
                else:
                    print(Guessed_char, "isn't in the word. Try again.")
                    Letters_Used += Guessed_char
                    Guesses += 1 
                    print("")
                    print(Guesses,"tries out of the",Tries,"left.")
                    print("")
                    print("The word so far is: ", Dashed_Word)
                    print("")
                    print("Letters Used:",Letters_Used)
                # conditonal is activated when all 6 tries are used.
                if Guesses == Tries and Dashed_Word != word:
                    print("")
                    print("You've used up all your 6 tries. YOU LOSE!")
                    print("")
                    print("The word was: ",word,)
                    break
                if Guesses == Tries and Dashed_Word == word:
                    print("")
                    print("You finished in the last attempt! Good Job!")
            #else conditional is activated if the input has numbers.
            else:
                print("")
                print("The character must include only alphabets.")
            #activated if the guessed word is equal to the hidden word.
            if Dashed_Word == word:
                print("")
                print("You guessed the entire word. YOU WIN! ")
                
# ENTIRE PROCESS IS REPEATED WITHIN MULTIPLE ELSE STATEMENTS.
    else:
        print("")
        print(" Numbers are not allowed in the input.") # prints error 
        Hidden_Word = input("Enter a word to be hidden: ")
    print("")
    #print("Phrase: ", Hidden_Word)
    # makes the code lowercase 
    Hidden_Word = Hidden_Word.lower()
    word = Hidden_Word
    # makes the number of dashes equal to the length of the word.
    Dashed_Word = "-" * len(Hidden_Word)
    if " " in Hidden_Word:
        Dashed_Word.replace("-"," ",len(Hidden_Word))
        Guesses = 0
        Letters_Used = ""
        Tries = 6
        while Guesses < Tries and Dashed_Word != word:
            print("")
         #   print("The word so far is: ", New_Dashed_Word)
            # makes an input
            Guessed_char = input("Enter a letter or word to guess: ")
            if Guessed_char.isalpha() or " " in Guessed_char:
                print("")
                Guessed_char = Guessed_char.lower()
                
                if Guessed_char in word:
                    if Guessed_char == word:
                        print("You guessed the exact word! YOU WIN!")
                        break;
                    print("Great job! That letter/phrase is in the word!")
                    Guesses += 1 
                    print("")
                    print(Guesses,"tries out of the",Tries,"left.")
                    print("")
                    Letters_Used += Guessed_char 
                  #  Updated_Word = ""
                    New_Dashed_Word=\
                    update_dash_word(Dashed_Word,word,Guessed_char)
                    print("The word so far is: ", New_Dashed_Word)
                    print("")
                    print("Letters Used:",Letters_Used)
                    Dashed_Word = New_Dashed_Word
                # else statement prints if the character isnt in the word.
                else:
                    print("Sorry,",Guessed_char, "isnt in the word. Try again")
                    Letters_Used += Guessed_char
                    Guesses += 1 
                    print("")
                    print(Guesses," tries out of the",Tries,"left.")
                    print("")
                    print("The word so far is: ", Dashed_Word)
                    print("")
                    print("Letters Used:",Letters_Used)
                # if the Word they try to guess isn't the hidden word within
                # the six tries the conditional is activated.
                if Guesses == Tries and Dashed_Word != word:
                    print("")
                    print("You've used up all your 6 tries. YOU LOSE!")
                    print("")
                    print("The word was",word,)
                if Guesses == Tries and Dashed_Word == word:
                    print("")
                    print("You finished in the last attempt! Good Job!")
            if len(Guessed_char) > 1 and Guessed_char != Hidden_Word:
                print("")
                print("You guessed the wrong word of the phrase. YOU LOSE!")
            elif len(Guessed_char) > 1 and Guessed_char == Hidden_Word:
                print("")
                print("You guessed the exact word! YOU WIN!")
            else:
                print("")
                print("The character guessed must include only alphabets.")
                
            if Dashed_Word == word:
                print("")
                print("You guessed the entire word. YOU WIN! ")
        
else:
    print("")
    print("The word to be guessed has to include only alphabets.")
    Hidden_Word = input("Enter a word to be hidden: ")
    print("")
    print("Phrase: ", Hidden_Word)
    Hidden_Word = Hidden_Word.lower()
    word = Hidden_Word
    Dashed_Word = "-" * len(Hidden_Word)
    Guesses = 0
    Letters_Used = ""
    Tries = 6
    while Guesses < Tries and Dashed_Word != word:
        print("")
     #   print("The word so far is: ", New_Dashed_Word)
    
        Guessed_char = input("Enter a letter or word to guess: ")
        if Guessed_char.isalpha() or " " in Guessed_char:
            print("")
            Guessed_char = Guessed_char.lower()
            
            if Guessed_char in word:
                if Guessed_char == word:
                    print("You guessed the exact word! YOU WIN!")
                    break;
                print("Great job! That letter/phrase is in the word!")
                Guesses += 1 
                print("")
                print("You made",Guesses,"attempts out of the",Tries,"left.")
                print("")
                Letters_Used += Guessed_char 
              #  Updated_Word = ""
                New_Dashed_Word=update_dash_word(Dashed_Word,word,Guessed_char)
                print("The word so far is: ", New_Dashed_Word)
                print("")
                print("Letters Used:",Letters_Used)
                Dashed_Word = New_Dashed_Word
                
            else:
                print("Sorry,",Guessed_char, "isn't in the word. Try again.")
                Letters_Used += Guessed_char
                Guesses += 1 
                print("")
                print("You made",Guesses,"attempts out of the",Tries,"left.")
                print("")
                print("The word so far is: ", Dashed_Word)
                print("")
                print("Letters Used:",Letters_Used)
                 
            if Guesses == Tries and Dashed_Word != word:
                print("")
                print("You've used up all your 6 tries. YOU LOSE!")
                print("")
                print("The word was",word,)
            if Guesses == Tries and Dashed_Word == word:
                print("")
                print("You finished in the last attempt! Good Job!")
            if len(Guessed_char) > 1 and Guessed_char != Hidden_Word:
                print("")
                print("You guessed the wrong word of the phrase. YOU LOSE!")
                break;
            elif len(Guessed_char) > 1 and Guessed_char == Hidden_Word:
                print("")
                print("You guessed the exact word! YOU WIN!")
        else:
            print("")
            print(" Numbers are not allowed in the input.")
            
        if Dashed_Word == word:
            print("")
            print("You guessed the entire word. YOU WIN! ")


        
        
    


    


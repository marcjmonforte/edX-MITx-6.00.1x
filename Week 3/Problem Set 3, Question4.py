# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    # Create a list of letters from secretWord.
    secretWord_list = list(secretWord)
    
    # Iterate through each letter from lettersGuessed
    for letter in lettersGuessed:
        
        # If letter is in there...
        if letter in secretWord_list:
            
            # While it remains in there (i.e. multiple instances), keep removing it until none left.
            while letter in secretWord_list:
                secretWord_list.remove(letter)
    
    # Return True if all letters were removed.
    return secretWord_list == []



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    '''
    
    # Create an empty list, which will hold your guesses.
    currentGuess_list = []
    
    # Index through each letter in secretWord, in order.
    for i in range(len(secretWord)):
        
        # If that letter is in the list of guessed letters...
        if secretWord[i] in lettersGuessed:
            
            # Add it to the current guesses list.
            currentGuess_list.append(secretWord[i] + ' ')
            
        else:
            # If not, add an underscore.
            currentGuess_list.append('_ ')
    
    # Concatenate all the items into a string.
    currentGuess = ''.join(currentGuess_list)
    
    return(currentGuess)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # Establish a list of letters in the alphabet.
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabetList = list(alphabet)
    
    # For the letters in the lettersGuessed list...
    for letter in lettersGuessed:
        
        # If the letter is still in the alphabet, remove it.
        if letter in alphabetList:
            alphabetList.remove(letter)
    
    # Return a concatenated string of the remaining letters.            
    updatedAlphabet = ''.join(alphabetList)
    return updatedAlphabet
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    # Establish necessary variables.    
    numGuesses = 8
    lettersGuessed = []
    
    # Introductory text, when starting the game.
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", str(len(secretWord)), "letters long.")
    
    # Game logic flow.
    while True:
        print("-------------")
        print("You have", numGuesses, "guesses left.")
        print("Available letters:", getAvailableLetters(lettersGuessed))
        userGuess = input("Please guess a letter: ")
        userGuess = userGuess.lower()
        
        # If the letter has already been guesssed, let user know.
        if userGuess in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
       
        # If the letter is correct, let user know.
        elif userGuess in secretWord:        
            lettersGuessed.append(userGuess)
            print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
        
        # If the letter is incorrect, reduce number of guesses and let user know.
        else:
            numGuesses -= 1
            lettersGuessed.append(userGuess)
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
        
        # If you run out of guesses, end game.
        if numGuesses == 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was", secretWord + ".")
            break
        
        # If you guess the word correctly, end game.
        elif isWordGuessed(secretWord, lettersGuessed) == True:
            print("------------")
            print("Congratulations, you won!")
            break

    
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
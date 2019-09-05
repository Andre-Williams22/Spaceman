import random
import os

guessed_word = ""
correct_guessed = []
unused_guessed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('wordstext.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
     
    for letters in secret_word:
        if letters in letters_guessed:
            return True
        else:
            return False
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    pass

def get_guessed_word(secret_word, letters_guessed):
    arr = []

    for letter in secret_word:
        if letter in letters_guessed:
            return arr.append(letter)
        else:
            return arr.append('_')
        # Joins the end of both of the arrays
        return ''.join(arr)
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores. For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    pass

def play_once_more():
    yes_or_no = input("Do you want to play another time y/n:  ")
    if 'y' in yes_or_no:
        return True
    else:
        return False




def is_guess_in_word(guess, secret_word):

    for letter in secret_word:
        if letter == guess:
            return True
        else:
            return False
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word

    pass




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    incorrect_guess = len(secret_word)

    #TODO: show the player information about the game according to the project spec
    print('Welcome to Spaceman user ')
    print('The secret word is {} letters long '.format(len(secret_word)))
    
    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    # get user input
    guess = input('please enter a letter: ')

    if len(guess) != 1:
        return ('please input one letter at a time')
    else:
        pass 

    print('You have {} many guesses left. Guess one letter per round '.format(incorrect_guess))
    

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
    
    #TODO: show the guessed word so far
    print('You have {} many guesses left. Guess one letter per round '.format(incorrect_guess))


    #TODO: check if the game has been won or lost






#These function calls will start the game
secret_word = load_word()
print(spaceman(secret_word))
print(play_once_more)
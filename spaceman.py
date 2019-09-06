import random
import os


def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('wordstext.txt', 'r')
    words_list = f.read().split(' ')
    f.close()

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
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    arr = []

    for letter in secret_word:
        if letter in letters_guessed:
            return arr.append(letter)
        else:
            return arr.append('_')
        # Joins the end of both of the arrays
        return ''.join(arr)


    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    pass



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

def play_once_more():
    yes_or_no = input("Do you want to play another time y/n:  ")
    if 'y' in yes_or_no:
        return True
    else:
        return False


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''


    guessed_word = " "
    correct_guessed = []
    unused_guess = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    incorrect_guess = len(secret_word)

    os.system('clear game')
    print('Welcome and enjoy a game Spaceman in the Terminal')
    print('The secret word contains: {} letters'.format(len(secret_word)))
    print('You have {} incorrect guesses left, please enter one letter per round'.format(
        incorrect_guess))
    # The essence of the game
    while True:

        #TODO: show the player information about the game according to the project spec

        # get user input
        guess = input('please enter a letter: ')

        #TODO: Ask the player to guess one letter per round and check that it is only one letter 
        if len(guess) != 1:
            return('please input one letter at a time')
        else:
            pass

        #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        if guess not in unused_guess:
            print('you already typed this word')
            pass
        # removes the guess from the list
        unused_guess.remove(guess)
        remaining_letters = ','.join(unused_guess)


        if incorrect_guess == 0:
            print('You lost the game.')
            print("the answer is {}".format(secret_word))
            break
        
        if is_guess_in_word(guess, secret_word):
        # adds the guess to a list
            correct_guessed.append(guess)

            guessed_word = get_guessed_word(secret_word, correct_guessed)

            print('guessed letters so far: {} '.format(guessed_word))
            print('You have not guessed these letters yet: {} '.format(remaining_letters))
            break

        if is_word_guessed(secret_word, correct_guessed):
            print('Congratualations you won the game')
            break


        else:
            # Get the letters that they have so far
            guessed_word = get_guessed_word(secret_word, correct_guessed)
                # Remove one off of the incorrect guess counter
            incorrect_guess -= 1
                # Print information and where they are at in the game
            print("Sorry, your guess was not in the word, try again. Guess one letter per round")
            print("You have {} incorrect guesses left".format(incorrect_guess))
            print("Guessed word so far: {}".format(guessed_word))
            print("These letters you haven't guessed yet:  {}".format(remaining_letters))



#starts the game
running = True
while running:
    secret_word = load_word()
    spaceman(load_word())
    running = play_once_more()
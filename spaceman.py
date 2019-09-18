import random
import os
import re
from colorama import Fore, Back, Style

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


def get_new_word(current_word):
    # Open the file again as we are going to get a new word from the list
    with open('wordstext.txt', 'r') as f:
        words_list = f.read().split(' ')

    # Oneline filter function that only gets words with a length of the current_word
    correct_len_words = filter(lambda x: len(
        x) == len(current_word), words_list)

    # Initalize a list for all the 'related' words in the list
    related_words = []
    # Loop through all the words in the length filtered list
    for word in list(correct_len_words):
        is_related = True  # Keep a variable to track related status of a letter
        # Get index and value for every letter in the current word
        for i, character in enumerate(current_word):
            if character.isalpha():  # Check if the character is alpha so that it ignores '_' characters
                # Set related to false if the letter in the word is not the same as the letter in current word
                if word[i] != character:
                    is_related = False
        if is_related:  # A check that will only add the word if related remains as true
            related_words.append(word)

    return related_words


def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    tell = []
    for letter in secret_word:
        if letter in letters_guessed:
            tell.append(letter)
        else:
            tell.append('_')
    return tell


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    for letter in secret_word:
        if letter == guess:
              return True
        else:
            return False
     
   # return [x for x in guess if x in secret_word]


def play_again():
    yes_or_no = input("Would you like to play again? y/n:  ")
    if "y".lower() in yes_or_no.lower():
        os.system('clear')
        return True
    else:
        os.system('clear')
        return False



def is_palindrome(s):
    if s == s[::-1]:
        return True
    return False



def spaceman(secret_word):
    guessCounter = 7

    while True:
        print('------------------------------------------')
        print(Fore.MAGENTA + 'Guess the Spaceman\'s word!' + Fore.RESET)
        print('\nCorrect letters: ')
        # If a letter is in correct_list it will replace the spot with the letter (i).
        for i in secret_word:
            if i in correct_list:
                # end=' ' Appends a space after the print statement
                print(i, end=' ')
            # If there isn't a correct letter it will print '_' in position of the secret_word
            else:
                print('_', end=' ')
        print('\n\nIncorrect letters: ')
        for i in incorrect_list:
            print(i, end=' ')

        print('\n-----------------------------------------')

        guess = user_input()
        guessCounter = guess_checker(guess, secret_word, guessCounter)
        win = win_checker(secret_word)

        if win == False:
            print(
                Fore.RED + f'\nYou lost! The word was: {secret_word}' + Fore.RESET)
            play_again()
            break
        elif win == True:
            print(
                Fore.GREEN + f'\nYou won! The word was: {secret_word}' + Fore.RESET)
            play_again()
            break
# These function calls that will start the game
if __name__ == '__main__':
    running = True
    while running:
        spaceman(load_word())
        running = play_again()
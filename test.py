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

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    # for letter in secret_word:
    #     if letter == guess:
    #         return True

    # return False
    return [x for x in guess if x in secret_word]

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
    return ''.join(tell)




def test_is_word_guessed():
    assert is_word_guessed('l','letter') == True, 'Wrong logic'

def test_get_guessed_word():
    assert get_guessed_word('apple', 'pple') == '_pple', 'incorrect logic'

def test_is_guessed_word():
    assert is_word_guessed('a', 'autonomy') == True, 'Wrong because a is in the word'



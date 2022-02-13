import random
import string

green = '\u001b[32m'
yellow = '\x1B[33m'
end_color = '\x1B[0m'

word_list = ['lucky', 'float', 'first', 'board', 'build']

chosen_word = random.choice(word_list)
available_letters = list(string.ascii_lowercase)


def display(guess, chosen_word, available_letters):
    '''
    guess is a string that the user guesses
    chosen_word is a string that is the correct answer
    available_letters: string, all unused letters

    returns guessed letters placed in the right spot will be green, 
    guessed letters in the wrong spot are yellow.
    '''

    guess_display = ''
    correct_letters = ''
    for index, letter in enumerate(guess):
        if guess[index] == chosen_word[index]:
            correct_letters += letter

    for index, letter in enumerate(guess):
        if guess[index] == chosen_word[index]:
            guess_display += f"{green}{letter}{end_color}"
        elif letter in chosen_word:
            guess_display += f"{yellow}{letter}{end_color}"
        else:
            guess_display += letter
            if letter in available_letters:
                available_letters.remove(letter)
    return guess_display


def wordle(chosen_word):
    '''
    attempts is the number of attempts the player has to guess 

    '''

    attempts = 6

    while attempts > 0:
        guess = input('Guess a 5 letter word ')

        if len(guess) != 5:
            print('Guess must be 5 letters')

        print(f'{display(guess, chosen_word, available_letters)}')
        if guess == chosen_word:
            print("You guessed it!!")
            
        attempts -= 1
        print(f"Remaining available letters:\n {' '.join(available_letters)}")
        print(f'You have {attempts} guesses left. \n')

    print(f'That was your last guess!! The correct word was {chosen_word}')


wordle(chosen_word)

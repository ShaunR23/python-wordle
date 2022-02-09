import random


word_list = ['lucky', 'float', 'first', 'board', 'build']

chosen_word = random.choice(word_list)
print(chosen_word)


tries = 0
# display= []


end_of_game = False

while end_of_game == False:
    guess = input("Guess a five letter word: ")
    # print(guess)
    tries += 1

    if guess == chosen_word:
        print(f'You guessed it in {tries}')
        end_of_game = True

    if tries == 6:
        print('out of tries')
        end_of_game = True

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        display = list(guess)
        if letter in guess:
            display[position] = letter.upper()
            guess = display
    print(display)
       

    

    
    

    
        


        






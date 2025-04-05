import random 
from words import words
import string 
from hangman_display import hangman_display 

def hangman():
    word = random.choice(words).upper() #chose a random word 
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase) #all alphabets
    used_letters = set() #user input letters

    lives = 6

 
    #input     
    while len(word_letters) > 0 and lives>0:

        print('used letters: ', ''.join(used_letters))
        word_disp = [letter if letter in used_letters else '_' for letter in word]
        print('word: ', ''.join(word_disp))
        print(hangman_display[6-lives])


        user_letter = input('guess a letter: ').upper()
        # if user input correct remove letter from word letter
        # otherwise put that in used letters 
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('letter is not in word')


        elif user_letter in used_letters:
            print('already used. try again.')
        elif user_letter not in alphabet:
            print('invalid input. try again')

    if lives==0:
        print(hangman_display[0])
        print(f'you lost. the word was {word}')
    else:
        print('hooray! you won.')

    play_again= input('do you wanna play again ? [y/n]').lower()
    if play_again == 'y':
        hangman()
    else:
        print('see you soon!')

        

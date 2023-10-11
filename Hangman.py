import random
import string

name = input('Enter your name: ')

print(f'Welcome to Hangman game {name.capitalize()}')
print('I will choose a word and you try guessing the letters of the word.\nGood Luck.\nHave Fun')

def get_word():
    #list of words for the computer to choose from
    words = ['python','java','javascript','csharp','Learning','Cool','FUN','happy','Hangman','ITHS','AI','MachineLearning']
    #choice method returns a random element from the words list
    return random.choice(words).lower()
    #comp_word_length = len(comp_word)

#defining a function if the user wants to play again
def play_again():
    res = input('Do you want to play? y/n:').lower()
    if res == 'y':
        hangman_game()
    else:
        print('See you next time.')

#defining game play function
def hangman_game():
    comp_word = get_word()
    
    comp_word_length = len(comp_word)
    guessed_letters = []
    #alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = string.ascii_lowercase
    no_of_tries = 10
    guessed = False
    print()
    print(f'The word contains {comp_word_length} no.of letters')
    print(comp_word_length* '_ ')
    print('You have '+str(no_of_tries)+' tries total')
    while guessed == False and no_of_tries>0:
        print('You have '+str(no_of_tries)+' tries left still')
        guess = input('enter a letter or word of your guess: ').lower()

        if len(guess)==1:
            if guess not in alphabet:
                print('please enter an alphabet not number')
            elif guess in guessed_letters:
                print('You already guessed that letter')
            elif guess in comp_word:
                print('Correct! That letter is in word')
                guessed_letters.append(guess)
            elif guess not in comp_word:
                print('That letter is not in the word')
                guessed_letters.append(guess)
                no_of_tries-=1
            else:
                print('wrong,try again')
        # elif len(guess) == len(comp_word):
        #     if guess == comp_word:
        #         print('You guessed it correctly')
        #         guessed = True
        #     else:
        #         print('your guess is not correct \ntry again')
        #         no_of_tries-=1
        else:
            print('Its more than one alphabet')
            no_of_tries-=1

        user_word=''

        if guessed == False:

            for letter in comp_word:
                if letter in guessed_letters:
                    user_word+=letter
                    
                else:
                    user_word+='_ '
            print(user_word)

        if user_word == comp_word:
            print(f'You guessed the word correctly {comp_word}')
            guessed=True
        elif no_of_tries==0:
            print('Sorry, You ran out of tries')

    play_again()

hangman_game()

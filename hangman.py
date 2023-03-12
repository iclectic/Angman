import random
import string
import nltk

nltk.download('words')

def get_valid_word():
    word_list = nltk.corpus.words.words()
    word = random.choice(word_list)
    while '-' in word or ' ' in word:
        word = random.choice(word_list)
    return word.upper()

def hangman():
    word = get_valid_word()
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed
    
    lives = 6
    
    #getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        
        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                # r
                
            else:
                lives = lives - 1 #takes away a life if wrong
                print('Letter is not in word') 
                
        elif user_letter in used_letters:
            print('You have already used that character.  Please try again')
        
        else: 
            print('Invalid character. Please try again.')
            
    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('Oops, it is all over. Sorry, the word was', word)
    else:
        print('You guessed the word', word, '!!')
    
    # prompt user to play again or quit
    play_again = input("Do you want to play again? Enter 'y' for yes or 'n' for no: ")
    if play_again.lower() == 'y':
        hangman()  # call hangman() function again to play again
    else:
        return  # exit function if user chooses to quit

hangman()

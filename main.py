
import random
from replit import clear


import hangman_words

word_list=hangman_words.word_list


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

import hangman_art

logo=hangman_art.logo

print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    clear()
    
    if guess in display:
        print(f"You have already guessed the {guess}. Try another letter.")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}. That's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    import hangman_art

    stages=hangman_art.stages
    print(stages[lives])
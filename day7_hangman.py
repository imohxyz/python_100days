import random
import day7_hangman_words
from day7_hangman_words import word_list
import day7_hangman_art
from day7_hangman_art import logo
from day7_hangman_art import stages

print(logo)
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('Game over')
    print(f"{' '.join(display)}")
    if '_' not in display:
        end_of_game = True
        print('You Win')
    print(stages[lives])
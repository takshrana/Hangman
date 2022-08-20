import random
from hangman_art import stages, logo
from hangman_words import word_list
from os import system, name


def clear():

    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in display:
        print(f"You've already tried guessing {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's wrong. You lose life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")
            k = input("")
    
    if not "_" in display:
        game_is_finished = True
        print("You win.")
        k = input("")

    print(stages[lives])

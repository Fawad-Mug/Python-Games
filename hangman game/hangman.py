from hangman_names import word_list
from hangman_art import logo, stages
import random
lives=6
end_of_game=False

chosen_word=random.choice(word_list)
print(chosen_word)

print(logo)

display=[]
for _ in range(len(chosen_word)):
    display += "_"


while not end_of_game:
    guess=input("Enter Guess Letter ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter



    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -=1
        if lives ==0:
            end_of_game= True
            print('You Lose')
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game=True
        print("You Win")
    print(stages[lives])
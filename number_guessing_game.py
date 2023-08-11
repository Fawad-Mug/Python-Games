# import random 
# print(f"Welcome to the number Guessing Game! \nI'm thinking of a number between 1 and 100")
# computer_choice=random.randint(1,100)
# difficulty_level=input("Choose a difficulty, Type 'easy' or 'hard':")

# chances=5
# if difficulty_level== 'easy':
#     chances+=5

# for i in range(chances):
#     print(f"You have {chances} attempts remaining toguess the number.")
#     guess=int(input('Make a guess: '))
#     if guess > computer_choice:
#         print("Too High.\nGuess again.")
#         chances-=1
#     elif guess < computer_choice:
#         print("Too Low.\nGuess again.")
#         chances-=1
#     elif guess == computer_choice:
#         print("You Won.")
#         break
# print(f'you are out of guesses')

    
############ 2nd method of tutuor

from random import randint
EASY_LEVEL=10
HARD_LEVEL=5

def check_answer(guess , computer_choice, turns):
    if guess > computer_choice:
        print("Too High.\nGuess again.")
        return turns-1
    elif guess < computer_choice:
        print("Too Low.\nGuess again.")
        return turns-1
    else:
        print(f"You got it! the answer is {computer_choice}.")


def set_difficulty():
    level=input("Choose a difficulty, Type 'easy' or 'hard':")
    if level=='easy':
        # global turns
        # turns=EASY_LEVEL
        return EASY_LEVEL
    else:
        # turns=HARD_LEVEL
        return HARD_LEVEL



def game():
    print(f"Welcome to the number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100")
    computer_choice=randint(1,100)



    turns= set_difficulty()

    guess= 0
    while guess!= computer_choice:
        print(f'You have {turns} attempts remaining to guess the number. ')
        guess=int(input('Make a guess: '))
        turns=check_answer(guess , computer_choice, turns)
        if turns==0:
            print(f'you ran out of guesses. You Lose')
            return

game()
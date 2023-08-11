import random 

def deal_cards():
    cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 10, 10, 10 ]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(score1, score2):
    if score2 == score1:
        return "Draw 😒"
    elif score1==0:
        return "Lose, opponent has Blackjack 😯"
    elif score2 ==0:
        return "Win with a Blackjack 😎"
    elif score2 > 21:
        return " You went over, You lose 😭"
    elif score1 > 21:
        return " Opponenet went over, You win 😋"
    elif score2 > score1:
        return "You win 😁"
    else:
        return"You Lose😥"


def play_game():
    user_cards= []
    computer_cards= []
    game_over = False  
    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())


    while not game_over:
        user_score= calculate_score(user_cards)
        computer_score= calculate_score(computer_cards)
        print(f" Your cards: {user_cards} , current score is {user_score}")
        print(f" Computer First card:{computer_cards[0]} ")
        if user_score ==0 or computer_score==0 or user_score>21:
            game_over= True
        else:
            another_card=input('Type "y" to get another card or "n" to pass: ')
            if another_card =="y":
                user_cards.append(deal_cards())
            else:
                game_over=True

    while computer_score!= 0 and computer_score<17:
        computer_cards.append(deal_cards())
        computer_score= calculate_score(computer_cards)


    print(f" Your final hand: {user_cards}, final score{user_score}")
    print(f" Computer's final hand: {computer_cards}, final score{computer_score}")
    print(compare_score(computer_score , user_score))

while input("Do you want to play a game of blackjack type 'y' otherwise 'n': ") == 'y':
    play_game()
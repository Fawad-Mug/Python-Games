rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random 
# computer= random.randint(0,2)
# user=int(input("Select 0 is Rock , 1 is Paper , 2 is Scissor"))
# if computer==0:
#   computer_select= rock 
# elif computer==1:
#     computer_select= paper
# elif computer==2:
#     computer_select=scissors
# if  user==0:
#   user_select= rock
# elif  user==1:
#     user_select= paper
# elif  user==2:
#     user_select= scissors
# if computer_select== user_select:
#    print(f'Its Draw')
# elif computer_select== scissors and user_select== rock:
#    print(f'You Win')
# elif computer_select== paper and user_select== scissors:
#    print(f'You Win')
# elif computer_select== rock and user_select==paper:
#    print(f'You Win')
# else:
#    print(f'You Lose')
# print(f'computer select{computer_select}')
# print(f'User select {user_select}')


# ///////2nd Method

images=[rock, paper, scissors]
computer_select=random.randint(0,2)
user_select=int(input("Select 0 is Rock , 1 is Paper , 2 is Scissor"))
print(images[computer_select])
print(images[user_select])
if user_select >=3 and user_select<0:
    print(f'You enter a invalid entry')
elif user_select==0 and computer_select==2:
    print(f'You Win')
elif user_select==2 and computer_select==0:
    print(f'You Loose')
elif user_select > computer_select:
    print(f'You Win')
elif user_select < computer_select:
    print(f'You Loose')
elif user_select == computer_select:
    print(f'its Draw')
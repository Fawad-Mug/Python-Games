from random import *
i=1
count=0
corr=0
n=randint(1,100)
while i>0:

    x=int(input('Enter Guess Number'))
    count+=1
    if x>n:
        print('Too, High Guess')
    elif n>x:
        print('Too, Low Guess')
    elif n==x:
        print('Congratulation, you Won')
        corr+=1
        a=input("If you Want To Play again then write Yes or No")
        print(f'Your Total tries:{count}')
        print(f'Your Correct Answer is:{corr}')
        if a=='Yes' or a=='YES' or a=='Y' or a=='y':
            print('Start')
            n=randint(1,100)
        else:
            break
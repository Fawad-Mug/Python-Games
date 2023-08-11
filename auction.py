# from replit import clear
# from art import logo
# print(logo)

bids={}

def winner_bid(bidding_record):
    maxi=0
    winer= ""
    for bidder in bidding_record:
        max_bid=bidding_record[bidder]
        if max_bid > maxi:
            maxi = max_bid
            winer = bidder
    print(f'THe wineer is {winer} with a bid os ${maxi}')


bid_finish=True
while bid_finish:
    name=input('Enter your name: ')
    price=int(input('what is your bid? $ '))
    bids[name]=price
    finish=input('Are you want to enter more bid Yes or no? \n')
    if finish=='no':
        bid_finish=True
        winner_bid(bids)
    #elif finish=='yes':
        #clear() #check this for google of clear console tab 
bidders = {}

more_bidders = "yes"
while more_bidders == "yes":
    name = input("What is your name? \n")
    bid  = input("What is your bid? \n")
    bidders[name] = bid
    more_bidders = input("Do you want to bid again? (yes/no)")
    if more_bidders == "no":
        highest_bid = 0
        for name in bidders:
            if int(bidders[name]) > highest_bid:
                highest_bid = int(bidders[name])
                winner = name

        print(f"The winner is {winner} with a bid of {highest_bid}")





    
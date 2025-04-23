# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo
print(logo)

# Function to find the highest bidder from the bidding records
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # Iterate over the dictionary to find the highest bid
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        # If the current bid is higher than the highest bid found so far, update the highest bid and the winner
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    # Announce the winner and the highest bid
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# Initialize an empty dictionary to store bids
bids = {}
# Flag to control the continuation of the bidding process
continue_bidding = True

while continue_bidding:
    # TODO-1: Ask the user for input (name and bid amount)
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    
    # TODO-2: Save data into dictionary {name: price}
    bids[name] = price
    
    # TODO-3: Ask if new bids need to be added
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    
    # If no other bidders, stop the bidding and find the highest bidder
    if should_continue == "no":
        continue_bidding = False
        # TODO-4: Compare bids in the dictionary and determine the highest bidder
        find_highest_bidder(bids)
    # If there are other bidders, clear the screen for the next input
    elif should_continue == "yes":
        print("\n" * 20)        # Clears the screen by printing multiple newlines

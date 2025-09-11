from art import logo

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

def validate_amount():
    amount = input("What's bid amount: $")

    while not amount.isnumeric():
        print("Please enter a positive number!")
        amount = input("What's bid amount: $")

    return float(amount)


def validate_answer():
    answer = input("Is there other bidder. Type 'yes' or 'no': ").lower()

    while answer != "yes" and answer != "no":
        answer = input("Is there other bidder? Type 'yes' or 'no': ").lower()

    return answer


def find_highest_bidder(data):
    max_bid = 0
    winner_name = ""

    for item in data:

        if data[item] > max_bid:
            max_bid = data[item]
            winner_name = item

    return [winner_name, max_bid]

# replace with logo
print(logo)

auction_house = {}
auction_continues = True

while auction_continues:

    name = input("What's bidder name: ")
    amount = validate_amount()
    auction_house[name] = amount

    new_bidder = validate_answer()

    if new_bidder == "no":
        auction_continues = False

winner, bid = find_highest_bidder(auction_house)

print(f"The winner is {winner} with ${bid:.2f}!")

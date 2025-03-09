from art import logo
print(logo)
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
record = {}
auction = True

def name_bid():
    name = input("What is your name? : ")
    bid = int(input("What is your bid? : $ "))
    record[name] = bid
name_bid()
# TODO-3: Whether if new bids need to be added
while auction == True:
    answer = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    if answer == "yes":
        print("\n"*100)
        name_bid()
        auction = True
    elif answer == "no":
        auction = False
    else:
        print("Please put yes or no. ")
# TODO-4: Compare bids in dictionary
def winner():
    highest = 1
    for key in record:
        if record[key] > highest:
            highest = record[key]
    print(f"The winner is {key} with a bid of $ {highest}")
winner()
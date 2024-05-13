from cards import hearts, diamond, spades, clubs, card_dictionary
import random

#dealer_hand =[]
user_hand = []

print("Welcome to Black Jack" +' '+ hearts +' ' + diamond +' '+ spades +' '+ clubs)
print("Enter 'S' to Start ")

#convert dictionary to list, shuffles and return new list
def extract_card_list (dictionary):
    for _, _ in dictionary.items():
        sampled_list = random.sample(list(dictionary),len(dictionary))
        return sampled_list

#initialise deals to user and computer
initial_hand_dealt = extract_card_list(card_dictionary) 
print(initial_hand_dealt)
user_hand = random.choices (initial_hand_dealt, k=2)
print("user hand", user_hand)
dealer_hand = random.choices (initial_hand_dealt, k=2)
print("dealer hand", dealer_hand)
print(f"{dealer_hand[0]} 'hidden card'")

deal = input('Enter deal, hit or stand')



def gameplay (hand_dealt,hand):

    if hand == 'hit':
        new_user_hand = user_hand.append(random.choice(initial_hand_dealt))
        print(new_user_hand)
        #computer_hand = random. choice (hand_dealt)

        #return computer_hand
        #print(computer_hand)
    else:
        hand == 'stand'
        computer_hand = random.choices (hand_dealt,k=3)
        print(computer_hand)

gameplay(hand_dealt=initial_hand_dealt, hand=deal)

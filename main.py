from cards import hearts, diamond, spades, clubs, card_dictionary
import random

#dealer_hand =[]
#user_hand = []

print("Welcome to Black Jack" +' '+ hearts +' ' + diamond +' '+ spades +' '+ clubs)
print("Enter 'S' to Start ")

#convert dictionary to list, shuffles and return new list
def extract_card_list (dictionary):
    for _, _ in dictionary.items():
        sampled_list = random.sample(list(dictionary),len(dictionary))
        return sampled_list
    

#initialise deals to user and computer
initial_hand_dealt = extract_card_list(card_dictionary) 
print("shuffled sample", initial_hand_dealt)

def hand_dealt_gen (init_hand_dealt_dictionary):
    user_hand = random.choices (init_hand_dealt_dictionary, k=2)
    return user_hand

user_hand_dealt = hand_dealt_gen (init_hand_dealt_dictionary=initial_hand_dealt)
print("user dealt", user_hand_dealt)
dealer_hand_dealt = hand_dealt_gen (init_hand_dealt_dictionary=initial_hand_dealt)
print("dealer dealt", dealer_hand_dealt)

#deal = input('Enter deal, hit or stand')

''' 

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

'''
from cards import hearts, diamond, spades, clubs, card_dictionary
import random


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

#assign 2 list items to user and computer at start of game
user_hand_dealt = hand_dealt_gen (init_hand_dealt_dictionary=initial_hand_dealt)
print("user dealt -->", user_hand_dealt)
dealer_hand_dealt = hand_dealt_gen (init_hand_dealt_dictionary=initial_hand_dealt)
print("dealer dealt -->", dealer_hand_dealt[0] +','+"[card hidden]")

#deal = input('Enter deal, hit or stand')




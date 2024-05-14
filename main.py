from cards import hearts, diamond, spades, clubs, card_dictionary
import random


print("Welcome to Black Jack" +' '+ hearts +' ' + diamond +' '+ spades +' '+ clubs)
print("Enter 'S' to Start ")

#convert dictionary to list,sample and return new dictionary
def extract_card_dict(dictionary):
    sampled_list = random.sample(list(dictionary.items()),len(dictionary))
    sampled_dictionary = dict(sampled_list)
    return sampled_dictionary

#new = extract_card_dict(card_dictionary)  


'''
#initialise deals to user and computer
initial_hand_dealt = extract_card_dict(card_dictionary)
print("shuffled sample", initial_hand_dealt)

def hand_dealt_gen (init_hand_dealt_dictionary):
    user_hand = random.choices (init_hand_dealt_dictionary, k=2)
    return user_hand

def sum_dealt_hand (list_param):
    sum_list = 0
    print("param", list_param)
    for cards_in_list in list_param:
        print(type(cards_in_list))

        if cards_in_list == 'Ace_one':
            cards_in_list = card_dictionary['Ace_one']
            print(cards_in_list)

            #list_param[cards_in_list] =1
            
            #sum_list += cards_in_list
           # return 
        
        elif cards_in_list == 'Ace_eleven':
            cards_in_list = card_dictionary['Ace_eleven']
            #list_param[cards_in_list] =11
            sum_list += int(cards_in_list)
            print(type(sum_list))
            return sum_list
        
        
       

        elif cards_in_list == 'Queen' or 'Jack' or 'Queen' or 'King':
            cards_in_list = card_dictionary['Queen']
            #list_param[cards_in_list] =10
            sum_list += cards_in_list
            return sum_list


             else:
            sum_list = cards_in_list + cards_in_list
            return sum_list

       

    

#assign 2 list items to user and computer at start of game
user_hand_dealt = hand_dealt_gen (init_hand_dealt_dictionary=initial_hand_dealt)
print("user dealt -->", user_hand_dealt)
dealer_hand_dealt = hand_dealt_gen (init_hand_dealt_dictionary=initial_hand_dealt)
print("dealer dealt -->", dealer_hand_dealt[0] +','+"[card hidden]")

x=sum_dealt_hand(list_param=user_hand_dealt)
print(x)


def gameplay(user_hand_dealt): #is_hit, is_stand
    deal = input(" Enter 'S' for stand & 'H' for hit").lower()
    if deal == 'hit':
        x=sum_dealt_hand(list_param=user_hand_dealt)
        print(x)

gameplay(user_hand_dealt)
'''



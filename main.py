from cards import hearts, diamond, spades, clubs, card_dictionary
import random


print("Welcome to Black Jack" +' '+ hearts +' ' + diamond +' '+ spades +' '+ clubs)
print("Enter 'S' to Start ")

#convert dictionary to list,sample and return new dictionary
def __card_dict__(dictionary, sample_size):
    sampled_list = random.sample(list(dictionary.items()),sample_size)
    sampled_dictionary = dict(sampled_list)
    return sampled_dictionary


#initialise deals to user and computer,#assign 2 list items to user and computer at start of game
sampled_card_dict = __card_dict__(card_dictionary,len(card_dictionary))
print("shuffled dict", sampled_card_dict)

#deals 2 cards to dealer and user at start of game  
def __init_hand_dealt__():
    init_dealer_hand = __card_dict__(sampled_card_dict, 1)
    print(f"dealer dealt -->, {init_dealer_hand.keys()}, [hidden card]")
    init_user_hand = __card_dict__(sampled_card_dict, 2)
    print("user dealt -->", init_user_hand.keys())
    return init_dealer_hand, init_user_hand

dealer_hand, user_hand = __init_hand_dealt__() 


print(f"{dealer_hand}\n{user_hand}")

#sums the values in a dealt hand stored in a dictionary
def __sum_init_dealt_hand__ (sum_dictionary):
    sum_values = 0
    for _ in sum_dictionary:
        sum_values = sum(sum_dictionary.values())
        return sum_values
        

x = __sum_init_dealt_hand__(user_hand)
y =__sum_init_dealt_hand__(dealer_hand)
print(x,'\n',y)

def __black_jack__(user_hand, dealer_hand):
    is_user_blackjack = __sum_init_dealt_hand__(user_hand)
    is_dealer_blackjack = __sum_init_dealt_hand__(dealer_hand)
    if is_user_blackjack == 21:
        print("Black Jack !! You Win!")
    elif is_dealer_blackjack ==21:
        print("Black Jack !! Dealer Win!")


__black_jack__(user_hand, dealer_hand)








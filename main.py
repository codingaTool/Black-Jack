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

#new = extract_card_dict(card_dictionary)  
def __init_hand_dealt__():
    init_dealer_hand = __card_dict__(sampled_card_dict, 1)
    print("dealer dealt -->", init_dealer_hand, ' + '"[hidden card]")
    init_user_hand = __card_dict__(sampled_card_dict, 2)
    print("user dealt -->", init_user_hand)
    return init_dealer_hand, init_user_hand

dealer, user = __init_hand_dealt__() 

print(dealer)
print(user)



#dealer_hand_dealt = hand_dealt_gen (init_hand_dealt_dictionary=initial_hand_dealt)
#print("dealer dealt -->", dealer_hand_dealt[0] +','+"[card hidden]")





'''


x=hand_dealt_gen(initial_hand_dealt)
print(x)





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
'''
       
'''
    


x=sum_dealt_hand(list_param=user_hand_dealt)
print(x)


def gameplay(user_hand_dealt): #is_hit, is_stand
    deal = input(" Enter 'S' for stand & 'H' for hit").lower()
    if deal == 'hit':
        x=sum_dealt_hand(list_param=user_hand_dealt)
        print(x)

gameplay(user_hand_dealt)
'''



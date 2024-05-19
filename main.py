from cards import hearts, diamond, spades, clubs, card_dictionary_complete
import random,os ,sys

dealer_hand = {}
user_hand = {}

print("WELCOME TO BLACK JACK" +' '+ hearts +' ' + diamond +' '+ spades +' '+ clubs)

#convert dictionary to list,sample and return new dictionary
def __card_dict__(dictionary, sample_size):
    sampled_list = random.sample(list(dictionary.items()),sample_size)
    sampled_dictionary = dict(sampled_list)
    return sampled_dictionary

#initialise deals to user and computer
sampled_card_dict = __card_dict__(card_dictionary_complete,len(card_dictionary_complete))
#print("shuffled dict", sampled_card_dict)

#deals 2 cards to dealer and user at start of game  
def __init_hand_dealt__(dictionary, numb_cards_dealt):
    init_dealer_hand = __card_dict__(dictionary, numb_cards_dealt)
    return init_dealer_hand

dealer_hand = __init_hand_dealt__(sampled_card_dict, 1)
user_hand = __init_hand_dealt__(sampled_card_dict, 2) 



#sums the values in a dealt hand stored in a dictionary
def __sum_init_dealt_hand__ (sum_init_dictionary):
    sum_values = 0
    for _ in sum_init_dictionary:
        sum_values = sum(sum_init_dictionary.values())
        return sum_values
        
def __black_jack__(in_user_hand, in_dealer_hand):
    is_user_blackjack = __sum_init_dealt_hand__(in_user_hand)
    is_dealer_blackjack = __sum_init_dealt_hand__(in_dealer_hand)
    if is_user_blackjack == 21:
        print("BLACK JACK !! YOU WIN!")
        __quit_game__()
    elif is_dealer_blackjack ==21:
        print("BLACK JACK !! DEALER WIN!")
        __quit_game__()


#function to clear the screen
def __clear_screen__():
    os.system('clear')

#Quit function
def __quit_game__():
    sys.exit()

def __game_money__():
    game_coins = int(input("ENTER YOUR BET: $"))
    if game_coins <=0:
        return sys.exit("NO MONEY, NO PLAY, BYE FELICIA !")
    else:
        return game_coins
    

#Add 1 card to user and dealer, reveal 2 dealer cards
def __add_hit__(dictionary):
    add_hit = False
    while not add_hit:
        hit = input("(H)IT or (S)TAND or (Q)UIT-->>:").lower()
        if 'h' in hit:
            __clear_screen__()
            new_dealer_hand = __card_dict__(dictionary, 2)
            new_user_hand = __card_dict__(dictionary, 1)
            print(new_dealer_hand)
            print(new_user_hand)
            dealer_hand.update(new_dealer_hand.items())
            user_hand.update(new_user_hand.items())
            print("DEALER HAND{} USER HAND{}".format(list(dealer_hand.keys()),list(user_hand.keys())))
            new_dealer_sum =__sum_init_dealt_hand__(dealer_hand)
            new_user_sum =__sum_init_dealt_hand__(user_hand)
            print("TOTAL: DEALER POINTS:{}\t PLAYER POINTS:{} ".format(new_dealer_sum,new_user_sum))
            #return new_dealer_sum, new_user_sum
            if new_dealer_sum >= 21:
                print("DEALER LOSE!....YOU WIN")
                __quit_game__()
            elif new_user_sum >= 21:
                print("DEALER WON...YOU LOSE")
                __quit_game__()
            elif new_dealer_sum >=21 and new_user_sum >= 21:
                print("THIS GAME IS A DRAW!")
                __quit_game__()
            elif new_user_sum<new_dealer_sum<=21:
                print("DEALER WON...YOU LOSE")
                __quit_game__()
            elif new_dealer_sum<new_user_sum<=21:
                print("DEALER LOSE...YOU WIN")
                __quit_game__()

            else:
                break
        elif 's' in hit:

            __clear_screen__()
            new_dealer_hand = __card_dict__(dictionary, 2)
            #new_user_hand = __card_dict__(dictionary, 1)
            print(new_dealer_hand)
            print(user_hand)
            dealer_hand.update(new_dealer_hand.items())
            #user_hand.update(new_user_hand.items())
            print("DEALER HAND{} USER HAND{}".format(list(dealer_hand.keys()),list(user_hand.keys())))
            new_dealer_sum =__sum_init_dealt_hand__(dealer_hand)
            new_user_sum =__sum_init_dealt_hand__(user_hand)
            print("TOTAL: DEALER POINTS:{}\t USER POINTS:{} ".format(new_dealer_sum,new_user_sum))
            if new_dealer_sum >= 21:
                print("DEALER LOSE!....YOU WIN")
                __quit_game__()
            elif new_user_sum >= 21:
                print("DEALER WON...YOU LOSE")
                __quit_game__()
            elif new_dealer_sum and new_user_sum >= 21:
                print("THIS GAME IS A DRAW!")
                __quit_game__()
            else:
                break
        elif 'q' in hit:
            __quit_game__()
        else: 
            add_hit =True
            break
    

def __gameplay__():

    start_coins = __game_money__()
    __clear_screen__()
    print("YOUR BET:${}".format(start_coins))

    print("\nDEALER HAND -->>[Hidden Card],{}\n\nPLAYER HAND -->>{}\n".format(list(dealer_hand),list(user_hand)))

    __black_jack__(user_hand, dealer_hand)

    __sum_init_dealt_hand__(dealer_hand)
    __sum_init_dealt_hand__(user_hand)

    __add_hit__(card_dictionary_complete)
    

     

#function to loop game
restart = False
while not restart:

    __gameplay__()
    
    restart_game = input("Play again?'Y' to continue 'N' to Quit").lower()
    if restart_game == 'y':
        __clear_screen__()
        continue
    elif restart_game == 'n':
        __quit_game__()

        












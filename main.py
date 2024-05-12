from cards import hearts, diamond, spades, clubs,black_jack_cards
import random


print("Welcome to Black Jack" +' '+ hearts +' ' + diamond +' '+ spades +' '+ clubs)
print("Enter 'S' to Start ")

init_dealer_hand = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


final_dealer_hand = random.sample(init_dealer_hand, 2)

print(final_dealer_hand)
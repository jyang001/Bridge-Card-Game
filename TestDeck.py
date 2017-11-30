# test for Deck ADT
from Deck import *

def TestDeck():
    print("\n Creating a deck of cards and dealing it... \n")
    d = Deck()
    for i in range(52):
        c = d.deal()
        print(c)

    print("\n Creating a deck of cards and shuffling it...\n")
    #Yang: Create a new deck
    
    d1 = Deck()
    d1.shuffle()
    for i in range(52):
        c = d1.deal()
        print(c)

    print("\nsize of the deck is: ", d1.size())
    #Yang: print size of deck after all the cards have been dealed to make sure
    #      the deal() worked well

TestDeck()        

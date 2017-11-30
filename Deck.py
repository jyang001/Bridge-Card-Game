import random
from Card import Card
  
class Deck(object):

    #------------------------------------------------------------

    def __init__(self):

        """ Theta(n) run-time efficiency
        post: Creates a 52 card deck in standard order"""

        cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                cards.append(Card(rank,suit))
        self.cards = cards # cards in the deck
        self._size = 52 # number of cards initally in a deck

    #------------------------------------------------------------

    def size(self):

        """Cards left, Theta(1) run-time efficiency
        post: Returns the number of cards in self"""
        
        return self._size

    #------------------------------------------------------------

    def deal(self):

        """Deal a single card, Theta(1) run-time efficiency
        pre:  self.size() > 0
        post: Returns the next card in self, and removes it from self."""

        assert self._size > 0

        card = self.cards.pop() # removing a card from the deck
        self._size -= 1 # update the number of cards in the deck
        
        return card

    #------------------------------------------------------------

    def shuffle(self):

        """Shuffles the deck, using Python's random module
        post: randomizes the order of cards in self"""

        random.shuffle(self.cards)

        #n = self._size()
        #cards = self.cards
        #for i,card in enumerate(cards):
        #    pos = randrange(i,n)
        #    cards[i] = cards[pos]
        #    cards[pos] = card

    #------------------------------------------------------------

    def addTop(self,card):

        """ adds a card to the top of the deck, Theta(1) run-time efficiency
        pre: card is of type Card
        post: card is added back to the top of the deck"""

        self.cards.append(card) # putting the card to the top of the deck
        self._size += 1 # incrementing the size of the deck

    #------------------------------------------------------------

    def addRandom(self,card):

        """ adds a card to the random place in the deck, Theta(1) run-time efficiency
        pre: card is of type Card
        post: card is added back to the deck, into random place"""

        place = random.randint(0,self._size) # getting a random position for the card to be place into
        self.cards.insert(place,card) # putting the card into place position in the deck
        self._size += 1 # incrementing the size of the deck

    #------------------------------------------------------------

    def addBottom(self,card):

        """ adds a card to the bottom of the deck, Theta(1) run-time efficiency
        pre: card is of type Card
        post: card is added back to the bottom of the deck"""
        
        self.cards.insert(0,card) # put the card to the bottom of the deck
        self._size += 1 # increment size of the deck

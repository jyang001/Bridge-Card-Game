# Hand.py
class Hand(object):

    """A labeled collection of cards that can be sorted"""

    #------------------------------------------------------------

    def __init__(self, label=""):

        """Create an empty collection with the given label."""

        self.label = label
        self.cards = []

    #------------------------------------------------------------

    def add(self, card):
        
        """ Add card to the hand """

        self.cards.append(card)

    #------------------------------------------------------------

    def sort(self):
        
        """ Arrange the cards in descending bridge order."""

        self.cards.sort()
        self.cards.reverse()

    #------------------------------------------------------------

    def dump(self):
        
        """ Print out contents of the Hand."""

        print(self.label + "'s Cards:")
        for c in self.cards:
            print("   ", c)

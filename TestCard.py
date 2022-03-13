# TestCard.py

import sys
import unittest

from Card import *


class RankTest(unittest.TestCase):  # GIVEN
    """ Tests Rank methods: rank() and rankName() """

    def testRanks(self):  # GIVEN
        """ creates cards of rank 1 through 13 of clubs and
    verifies that the created card's rank is equal to the
    rank it was created with """

        for i in range(2, 15):
            myCard = Card(i, 'c')
            self.assertEqual(myCard.rank(), i)  # verifies that the card's rank is 'i'

    # Yang: wrote to test that the RankName matches number assigned
    def testRankNames(self):
        """test the names of the rank function 'rankName(...)' """
        RN = ['Two', 'Three', 'Four', 'Five', 'Six',
              'Seven', 'Eight', 'Nine', 'Ten',
              'Jack', 'Queen', 'King', 'Ace']
        s = "c"  # testing rank not suit
        for r in range(2, 14):
            myCard = Card(r, s)
            self.assertEqual(myCard.rankName(), RN[r - 2])  # index of rank - 2


class SuitTest(unittest.TestCase):
    """ Tests Suit methods: suit() and suitName() """

    # Yang: wrote to test the suit of the Card
    def testSuits(self):
        r = 10  # Yang: assign rank to one value since we only need to test suit
        for s in "cdhs":
            myCard = Card(r, s)
            self.assertEqual(myCard.suit(), s)

    ##Yang: wrote test the name of the suit
    def testSuitNames(self):

        """ creates cards of rank ...  of c (clubs), d (diamonds),
    h(hearts) and s (spades), and verifies that the created card's suit
    is equal to the suit it was created with (c,d,h,s) """

        r = 10
        i = -1
        sn = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        for s in "cdhs":
            i += 1
            myCard = Card(r, s)
            self.assertEqual(myCard.suitName(), sn[i])


def main(argv):
    unittest.main()


if __name__ == '__main__':
    main(sys.argv)

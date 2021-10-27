import collections
from random import choice

# This example demonstrates the power of implementing just two special methods:
#   __getitem__ and __len__

# The first thing to note is the use of collections.namedtuple to construct a simple class to represent individual cards
# We use namedtuple to build classes of objects that are just bundles of attributes with no custom methods,
# like a database record.
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# sorting
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    deck = FrenchDeck()
    print(len(deck))  # 52

    print('Get the first and the last card')
#     Reading specific cards from the deck—say, the first or the last—is easy, thanks to the __getitem__ method:
    print(deck[0])   # Card(card='2', suite='spades')
    print(deck[-1])  # Card(card='A', suite='hearts')

#     Pick a random card
    print("Pick a random card:")
    print(choice(deck))

#     Because our __getitem__ delegates to the [] operator of self._cards, our deck automatically supports slicing.
    print('Slicing example')
    print(deck[:3])
    print(deck[12::13])  # starting at index 12 and skipping 13 cards at a time

#     sort
    for card in sorted(deck, key=spades_high):
        print(card)

from itertools import product
import random
from const import SUITS, RANKS, CARD_PICTURES

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.points = self._determine_points()
        self.picture = CARD_PICTURES[self.rank]

    def _determine_points(self):
        if self.rank.isdigit():
            return int(self.rank)
        elif self.rank == 'ace':
            return 11
        return 10

    def __str__(self):
        return f"{self.rank} of {self.suit.capitalize()}"
        
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit, rank in product(SUITS, RANKS)]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

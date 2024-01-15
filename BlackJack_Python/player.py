import abc
import random
from deck import Card
from utils import get_input_with_validator

class Player(abc.ABC):
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.bet = 0
        self.money = 100

    @property
    def points(self):
        return sum(card.points for card in self.hand)

    def add_card(self, card: Card):
        self.hand.append(card)

    @abc.abstractmethod
    def would_like_to_hit(self):
        pass

    @abc.abstractmethod
    def place_bet(self, min_bet, max_bet):
        pass

    def __str__(self):
        cards = ", ".join(str(card) for card in self.hand)
        return f"{self.name}\nCards: {cards}\nPoints: {self.points}\n"

class HumanPlayer(Player):
    def would_like_to_hit(self):
        return get_input_with_validator(
            'Want new card?(y/n) ', lambda x: x in ['y', 'n']) == 'y'

    def place_bet(self, min_bet, max_bet):
        self.bet = get_input_with_validator(
            'Make your bet: ', 
            lambda x: x.isdigit() and min_bet <= int(x) <= max_bet, 
            error_message=f"Bets must be between ${min_bet} and ${max_bet}."
        )
        self.bet = int(self.bet)
        self.money -= self.bet

class AIPlayer(Player):
    def __init__(self, name, min_bet, max_bet):
        super().__init__(name)
        self.min_bet = min_bet
        self.max_bet = max_bet
        self.max_points = random.randint(17, 20)
    
    def would_like_to_hit(self):
        return self.points < self.max_points

    def place_bet(self, min_bet, max_bet):
        self.bet = random.randint(self.min_bet, self.max_bet)
        self.money -= self.bet

class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")
    
    def would_like_to_hit(self):
        return self.points < 17

    def place_bet(self, min_bet, max_bet):
        raise ValueError("Dealer does not place a bet.")
    
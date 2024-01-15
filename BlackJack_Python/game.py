from deck import Deck
from player import HumanPlayer, AIPlayer, Dealer
from utils import get_input_with_validator, NAMES

class Game:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.players = [HumanPlayer("You")]
        self._setup_bots()

    def _setup_bots(self):
        num_bots = get_input_with_validator(
            'Hello, write bots count ',
            lambda x: x.isdigit() and 0 <= int(x) <= 3,
            error_message="Number of bots must be between 0 and 3."
        )
        for i in range(int(num_bots)):
            self.players.append(AIPlayer(NAMES[i], min_bet=1, max_bet=20))

    def start_game(self):
        self.deck.shuffle()
        self._take_bets()
        self._deal_initial_cards()
        self._print_player_hands()
        self._play_players_turn()
        self._play_dealer_turn()
        self._resolve_bets()

    def _take_bets(self):
        for player in self.players:
            player.place_bet(1, 20)

    def _deal_initial_cards(self):
        for _ in range(2):
            for player in self.players + [self.dealer]:
                card = self.deck.deal_card()
                player.add_card(card)

    def _print_player_hands(self):
        for player in self.players:
            print(player)

    def _play_players_turn(self):
        for player in self.players:
            while not player.points > 21 and player.would_like_to_hit():
                card = self.deck.deal_card()
                player.add_card(card)
                print(player)
                if player.points > 21:
                    print(f"{player.name} busts!")
                    self.players.remove(player)

    def _play_dealer_turn(self):
        while self.dealer.would_like_to_hit():
            self.dealer.add_card(self.deck.deal_card())
        print(self.dealer)

    def _resolve_bets(self):
        dealer_points = self.dealer.points
        dealer_bust = dealer_points > 21

        for player in self.players:
            if player.points > 21:
                continue
            if dealer_bust or player.points > dealer_points:
                print(f"{player.name} wins!")
                player.money += player.bet * 2
            elif player.points == dealer_points:
                print(f"{player.name} pushes.")
                player.money += player.bet
            else:
                print(f"{player.name} loses.")

    @staticmethod
    def ask_to_continue(message):
        return get_input_with_validator(message, lambda x: x in ['y', 'n']) == 'y'

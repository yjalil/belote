import random
from belote.card import Card
from belote.hand import Hand
from belote.player import Player
from belote.deck import Deck

class BeloteGame:
    def __init__(self):
        self.table_card = None
        self.trump_suit = None
        self.human_player = Player('Human', human = True)
        self.players = [self.human_player, Player('Computer_1'), Player('Computer_2'),Player('Computer_3')]
        random.shuffle(self.players)
        self.hand_size = 5
        self.deck = Deck()
        self.round = 0
        self.gameover = False

    def show_me_table(self,card_str):
        self.table_card = self.deck.pick_card(card_str)
        print('---------Table card picked -----------')
        return self

    def show_me_human_hand(self,cards_str):
        self.human_player.hand = Hand([str(self.deck.pick_card(card)) for card in cards_str])

        print('---------Human cards picked -----------')
        return self

    def first_dealing(self):
        for player in self.players:
            if not player.human :
                player.hand = Hand([str(self.deck.pick_card()) for i in range(self.hand_size)])
                print('---------Bot cards picked -----------')
        return self

    def bidding_round(self):
        self.round += 1
        bids = []
        for player in self.players:
            print(f'------Round {self.round} : {player.name} to play-------')
            bids.append(player.makes_choice(self))
            if bids[-1] == 'take':
                print(f"Round {self.round} is over.")
                return self.gameover


        if bids == ['pass' for i in range(5)]:
            if self.round == 1:
                print(f"{self.round} is over.")
                return self.gameover
            else :
                print(f"The game is over.")
                self.gameover = True
                return self.gameover

    def second_dealing(self):
        for player in self.players:
            if player.bidder:
                for i in range(2):
                    player.hand.add_card(str(self.deck.pick_card()))
                player.hand.add_card(str(self.table_card))
                self.table_card = None
            else :
                for i in range(3):
                    player.hand.add_card(str(self.deck.pick_card()))
        return self

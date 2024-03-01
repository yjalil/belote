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
        print(str(self.table_card))
        return self



    def show_me_human_hand(self, cards_str):
        self.human_player.hand = Hand([str(self.deck.pick_card(card)) for card in cards_str])

        print('---------Human cards picked -----------')
        for card in self.human_player.hand.cards:
            card.update_score(self.trump_suit)
            print(f"{card} - Score: {card.score}")

        return self

    def first_dealing(self):
        for player in self.players:
            if not player.human:
                player.hand = Hand([str(self.deck.pick_card()) for i in range(self.hand_size)])
                print('---------Bot cards picked -----------')
                for card in player.hand.cards:
                    card.update_score(self.trump_suit)
                    print(f"{card} - Score: {card.score}")

        return self


    def bidding_round(self):
        self.round += 1
        bids = []
        for player in self.players:
            print(f'------Round {self.round} : {player.name} to play-------')
            bids.append(player.makes_choice(self))
            if bids[-1] == 'take':
            #    print(f"{player.name} have taken {self.trump_suit} as the trump suit.")
               print(f"Round {self.round} is over.")

               return self.gameover

        all_pass = all(bid == 'pass' for bid in bids)
        if all_pass:
           print(f"All players passed. Redoing the bidding round...")
           self.trump_suit = None
           bids = []
           for player in self.players:
               print(f'------Round {self.round} : {player.name} to play-------')
               bids.append(player.makes_choice(self))
               if player.human:
                  if bids[-1] == 'take':
                      remaining_suits = [suit for suit in self.deck.suits if suit != self.trump_suit]
                      suit_choice = input(f"Choose a suit from {', '.join(remaining_suits)}: ").lower()
                      self.trump_suit = suit_choice
                    #   print(f"{player.name} have taken {self.trump_suit} as the trump suit.")
                      break

               else:
                     if bids[-1] == 'take':
                       remaining_suits = [suit for suit in self.deck.suits if suit != self.trump_suit]
                       self.trump_suit = random.choice(remaining_suits)
                    #    print(f"{player.name} have taken {self.trump_suit} as the trump suit.")
                       break


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

        for player in self.players:
            print(f"Hand of {player.name}: {player.hand}")

        return self


    def play_trick(players, trick_winner_index, trump_suit):
        leading_card = None
        trick_winner_index = trick_winner_index
        current_player_index = trick_winner_index

        for _ in range(len(players[0].hand) - 1):
             current_player = players[current_player_index]
             played_card = current_player.play_card(leading_card, trump_suit)

             if leading_card is None:
               leading_card = played_card

             if played_card.beats(leading_card, trump_suit):
                trick_winner_index = current_player_index
                leading_card = played_card

             current_player_index = (current_player_index + 1) % len(players)

             trick_winner = players[trick_winner_index]
             trick_winner.add_trick(leading_card)

        return trick_winner_index

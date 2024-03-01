import random


class Player:
    def __init__(self,name,human = False) -> None:
        self.name = name
        self.hand = None
        self.bid = None
        self.score = 0
        self.suits = []
        self.human = human
        self.bidder = False



    def makes_choice(self, game):
       if self.human:
           bid = input("Your turn to bid. Pass or Take? ").lower()
       else:
          bid = random.choice(['take', 'pass'])

       print(f"{self.name} chose to {bid}")


       if game.round == 1 :
            if bid == 'take':
                self.bidder = True
                print(f"{self.name} have taken {game.table_card.suit} as the trump suit.")
                game.trump_suit = game.table_card.suit
                return bid


    def play_card(self, leading_card, trump_suit):
        if self.human:
            print(f"{self.name}, it's your turn to play.")
            card_index = int(input("Choose a card to play (enter index): "))
            return self.hand.cards.pop(card_index)
        else:
            # Implement bot logic to choose a card to play

            return random.choice(self.hand.cards)

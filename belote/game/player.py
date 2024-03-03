import random


class Player:
    def __init__(self,name,human = False) -> None:
        self.name = name
        self.hand = None
        self.score = 0
        self.suits = []
        self.human = human
        self.bidder = False

    def makes_choice(self, game ):
        if self.human:
            bid = input("Your turn to bid. Pass or Take? ").lower()

        else :
            bid = random.choice(['take','pass'])

        print(f"{self.name} chose to {bid}")

        if game.round == 1 :
            if bid == 'take':
                self.bidder = True
                print(f"{self.name} have taken {game.table_card.suit} as the trump suit.")
                game.trump_suit = game.table_card.suit
                return bid

            return bid

        else :
            if bid == 'take':
                self.bidder = True
                remaining_suits = game.deck.suits
                remaining_suits.remove(game.trump_suit)

                if self.human :
                    suit_choice = input(f"Choose a suit from {'/'.join(remaining_suits)}").lower()
                    game.trump_suit = suit_choice
                    print(f"{self.name} have taken {game.trump_suit} as the trump suit.")
                    return bid

                else :
                    game.trump_suit = random.choice(remaining_suits)
                    print(f"{self.name} have taken {game.trump_suit} as the trump suit.")
                    return bid

            return bid

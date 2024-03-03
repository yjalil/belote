import random
from belote.game.card import Card

class Deck :
    def __init__(self) -> None:
        self.suits = ['k7el', 'copas', 'chbada', 'dheb']
        self.values = ['4','5','cabal','dix','neuf','las','rey','sota']
        self.cards = []
        self.picks = []
        for s in self.suits:
            for v in self.values:
                self.cards += [Card('_'.join([s,v]))]
        self.cards_str = [str(card) for card in self.cards]
        self.picks_str = [str(card) for card in self.picks]

    def __str__(self) -> str:
        return ', '.join([str(card) for card in self.cards])

    def pick_card(self, card_str = None):
        if card_str:
            card = Card(card_str)
            if card in self.picks:
                print(f'{card_str} has already been picked and no longer in the deck')
                return self
        else :
            card = random.choice(self.cards)

        self.cards.remove(card)
        self.picks += [card]
        self.cards_str = [str(card) for card in self.cards]
        self.picks_str = [str(card) for card in self.picks]
        # print(len(self.cards))
        return card

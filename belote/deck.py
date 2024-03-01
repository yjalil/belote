import random
from belote.card import Card

class Deck :
    def __init__(self) -> None:
        self.suits = ['k7el', 'copas', 'chbada', 'dheb']
        self.values = ['las','4','5','neuf','dix','sota','cabal','rey']
        self.cards = []
        self.picks = []
        for s in self.suits:
            for v in self.values:
                self.cards += [Card('_'.join([s,v]))]
        self.cards_str = [str(card) for card in self.cards]
        self.picks_str = [str(card) for card in self.picks]

    def __str__(self) -> str:
        return ', '.join([str(card) for card in self.cards])




    def pick_card(self, card_str=None):
        # print("Current cards in deck:", self.cards_str)
        # print("Received card_str:", card_str)
        if card_str:
            card = Card(card_str)
            if card in self.cards:
                self.cards.remove(card)
                self.picks += [card]
                self.cards_str = [str(card) for card in self.cards]
                self.picks_str = [str(card) for card in self.picks]
                print(len(self.cards))
                # print("Card picked successfully.")
                # print("Remaining cards in deck:", self.cards_str)
                return card
            else:
                print(f'{card_str} is not in the deck')
        else:
            card = random.choice(self.cards)
            self.cards.remove(card)
            self.picks += [card]
            self.cards_str = [str(card) for card in self.cards]
            self.picks_str = [str(card) for card in self.picks]
            print(len(self.cards))
            # print("Random card picked successfully.")
            # print("Remaining cards in deck:", self.cards_str)
            return card


        #else:
           #card = random.choice(self.cards)
           #self.cards.remove(card)
           #self.picks.append(card)
           #print(len(self.cards))
           #print("Card picked successfully.")
           #return card  #

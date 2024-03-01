class Card:

    SCORES = {'las': 11, '4': 0, '5': 0, 'neuf': 0, 'dix': 10, 'sota': 2, 'cabal': 3, 'rey': 4}

    def __init__(self, card_str) -> None:
        self.suit = card_str.split('_')[0]
        self.value = card_str.split('_')[1]
        self.score = 0

    def __str__(self) -> str:
        return str(self.suit) + '_' + str(self.value)

    #def __eq__(self, other):
        #return self.suit == other.suit and self.value == other.value


    def beats(self, other_card, trump_suit):
        if self.suit == other_card.suit:
            return self.score > other_card.score
        elif self.suit == trump_suit:
            return True
        else:
            return False


    def update_score(self, trump_suit: str) -> int:

        if self.value == 'neuf':
            return 14 if self.suit == trump_suit else 0
        elif self.value == 'sota':
            return 20 if self.suit == trump_suit else 2
        else:
            return self.SCORES.get(self.value, 0)

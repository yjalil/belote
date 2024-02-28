class Card:
    def __init__(self, card_str) -> None:
        self.suit = card_str.split('_')[0]
        self.value = card_str.split('_')[1]

    def __str__(self) -> str:
        return str(self.suit) + '_' + str(self.value)

    def __eq__(self, other):
        return self.suit == other.suit and self.value == other.value

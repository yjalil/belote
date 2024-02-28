from belote.card import Card

class Hand:
    def __init__(self, cards_str = None) -> None:
        self.cards = [Card(card_str) for card_str in cards_str]


    def __str__(self) -> str:
        return ",".join([str(card) for card in self.cards])

    def add_card(self, card_str):
        self.cards += [Card(card_str)]
        return self

    def remove_card(self, card_str):
        self.cards.remove(Card(card_str))
        return self

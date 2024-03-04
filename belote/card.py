class Card:

    SCORES = {'las': 11, '4': 0, '5': 0, 'neuf': 0, 'dix': 10, 'sota': 2, 'cabal': 3, 'rey': 4}

    def __init__(self, card_str) -> None:
        split_card = card_str.split('_')
        if len(split_card) != 2:
            raise ValueError("Invalid card string format")
        self.suit = card_str.split('_')[0]
        self.value = card_str.split('_')[1]
        self.score = 0

    def __str__(self) -> str:

        # print("Calling __str__ method of Card class")
        return str(self.suit) + '_' + str(self.value)



    def __eq__(self, other):
        return self.suit == other.suit and self.value == other.value


    # def beats(self, other_card, trump_suit):
    #     if self.suit == other_card.suit:
    #         return self.score > other_card.score
    #     elif self.suit == trump_suit:
    #         return True
    #     else:
    #         return False


    def beats(self, other_card, trump_suit):
        if self.suit == trump_suit and other_card.suit != trump_suit:
            return True  # Trump card beats non-trump card
        elif other_card.suit == trump_suit and self.suit != trump_suit:
            return False  # Non-trump card loses to trump card
        elif self.suit == other_card.suit:
            return self.score > other_card.score  # Higher score card beats lower score card
        else:
            return False


    def update_score(self, trump_suit: str) -> int:
        self.score =  self.SCORES.get(self.value, 0)
        # print(self.SCORES[self.value])

        if self.value == 'neuf':
            if self.suit == trump_suit :
                self.score = 14

        elif self.value == 'sota':
            if self.suit == trump_suit :
                self.score = 20
            else :
                self.score = 2

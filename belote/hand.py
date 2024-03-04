from belote.card import Card

class Hand:
    def __init__(self, cards_str = None) -> None:
        self.cards = [Card(card_str) for card_str in cards_str]


    def __str__(self) -> str:
        return ",".join([str(card) for card in self.cards])


    # def add_card(self, card_str):
    #     if card_str is not None:
    #         self.cards += [Card(card_str)]
    #         #self.cards += [Card(self.table_card)]
    #     else:
    #         print("Invalid card string:", card_str)



    def add_card(self, card_str):
        #print("Received card string:", card_str)
        if isinstance(card_str, str):
           self.cards.append(Card(card_str))
        elif isinstance(card_str, Card):
            self.cards.append(card_str)
        else:
          raise ValueError("Invalid card format")


    # def remove_card(self, card_str):
    #      print("Before removal:", self.cards) # Print current list of cards
    #      try:
    #        self.cards.remove(Card(card_str)) # Attempt removal
    #      except ValueError:
    #        print("Card not found in hand:", card_str)  # Print error message if removal fails
    #      print("After removal:", self.cards)


    # def remove_card(self, played_card, hand, current_player_index):
    #     if played_card in hand[current_player_index]:
    #        hand[current_player_index].remove(played_card)
    #        print(f"Card {played_card} removed from hand.")
    #     else:
    #         print(f"Card {played_card} not found in hand.")


    # def remove_card(self, card_str, hand):
    #     if card_str in [str(card) for card in hand.cards]:
    #        self.cards = [card for card in hand.cards if str(card) != card_str]
    #        print(f"Card {card_str} removed from hand.")
    #     else:
    #        print(f"Card {card_str} not found in hand.")


    def remove_card(self, played_card):
      if played_card in self.cards:
         self.cards.remove(played_card)
         print(f"Card {played_card} removed from hand.")
      else:
         print(f"Card {played_card} not found in hand.")


    def __len__(self):
        return len(self.cards)

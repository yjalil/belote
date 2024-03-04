import random


class Player:
    def __init__(self,name,human = False,scores=None) -> None:
        self.name = name
        self.hand = None
        self.bid = None
        self.score = 0
        self.suits = []
        self.human = human
        self.bidder = False
        self.SCORES = scores or {'las': 11, '4': 0, '5': 0, 'neuf': 0, 'dix': 10, 'sota': 2, 'cabal': 3, 'rey': 4}
        self.collected_cards = []


    # def collect_cards(self, trick_cards, current_player_index):
    #     #for player, played_card in trick_cards:
    #     for player, played_card, current_player_index in trick_cards:
    #         player.hand.remove_card(str(played_card), player.hand, current_player_index)


    # def collect_cards(self, trick_cards, current_player_index):
    #     for player, played_card, current_player_index in trick_cards:
    #         player.hand.remove_card(str(played_card), player.hand)


    # def collect_cards(self, trick_cards):
    #    for player, played_card in trick_cards:
    #        player.hand.remove_card(str(played_card), player.hand)


    def collect_cards(self, trick_cards):
        for player, played_card in trick_cards:
          player.collected_cards.append(played_card)


#     def valid_cards(self, leading_card, trump_suit):
#         valid_cards = []

#         # Check if the player has a card of the same suit as the leading card
#         for card in self.hand.cards:
#             if card.suit == leading_card.suit:
#                 valid_cards.append(card)

#         # If the player doesn't have a card of the same suit, check for trump cards
#         if not valid_cards and trump_suit:
#             for card in self.hand.cards:
#                 if card.suit == trump_suit:
#                     valid_cards.append(card)

#         # If the player doesn't have a card of the same suit or a trump card, all cards are valid
#         if not valid_cards:
#             valid_cards = self.hand.cards

#         return valid_cards
# #*******
    # def makes_choice(self, game):
    #    if self.human:
    #        bid = input("Your turn to bid. Pass or Take? ").lower()
    #    else:
    #       bid = random.choice(['take', 'pass'])

    #    print(f"{self.name} chose to {bid}")


    #    if game.round == 1 and game.trump_suit is not None:  # Check if it's the first round and the trump suit is already set
    #       if bid == 'take':
    #          self.bidder = True
    #          game.trump_suit = game.table_card.suit
    #          print(f"{self.name} have taken {game.trump_suit} as the trump suit.")

    #    elif game.round == 1 and game.trump_suit is None:  # First round but trump suit is not set yet
    #      if bid == 'take':
    #         self.bidder = True
    #         #remaining_suits = [suit for suit in game.deck.suits]
    #         #suit_choice = input(f"Choose a suit from {', '.join(remaining_suits)}: ").lower()
    #         #suit_choice = random.choice(remaining_suits)
    #         #game.trump_suit = suit_choice
    #         game.trump_suit = game.table_card.suit
    #         print(f"{self.name} have taken {game.trump_suit} as the trump suit.")
    #    else:  # Redo bidding
    #       if bid == 'take':
    #          self.bidder = True
    #          if not self.human:  # Only if the player is not human, choose a random suit
    #             remaining_suits = [suit for suit in game.deck.suits]
    #             game.trump_suit = random.choice(remaining_suits)
    #             print(f"{self.name} have taken {game.trump_suit} as the trump suit.")
    #          else:  # If the player is human, let them choose the suit
    #             remaining_suits = [suit for suit in game.deck.suits]
    #             suit_choice = input(f"Choose a suit from {', '.join(remaining_suits)}: ").lower()
    #             game.trump_suit = suit_choice
    #             print(f"{self.name} have taken {game.trump_suit} as the trump suit.")

    #    return bid

#****


    # def makes_choice(self, game):
    #    if self.human:
    #       if game.round == 1 and game.trump_suit is None:
    #          bid = input("Your turn to bid. Pass or Take? ").lower()
    #          if bid == 'take':
    #             self.bidder = True
    #             remaining_suits = [suit for suit in game.deck.suits]
    #             suit_choice = input(f"Choose a suit from {', '.join(remaining_suits)}: ").lower()
    #             game.trump_suit = suit_choice
    #             print(f"{self.name} have taken {game.trump_suit} as the trump suit.")
    #          else:
    #             bid = 'pass'  # Ensure 'pass' is chosen if the human player doesn't take
    #       else:
    #         bid = input("Your turn to bid. Pass or Take? ").lower()
    #    else:
    #      bid = random.choice(['take', 'pass'])

    #    print(f"{self.name} chose to {bid}")

    #    if game.round == 1 and game.trump_suit is not None:  # Check if it's the first round and the trump suit is already set
    #      if bid == 'take':
    #         self.bidder = True
    #         game.trump_suit = game.table_card.suit
    #         print(f"{self.name} have taken {game.trump_suit} as the trump suit.")

    #    elif game.round == 1 and game.trump_suit is None:  # First round but trump suit is not set yet
    #       if bid == 'take':
    #          self.bidder = True
    #          game.trump_suit = game.table_card.suit
    #          print(f"{self.name} have taken {game.trump_suit} as the trump suit.")

    # #    else:  # Redo bidding
    # #      if bid == 'take':
    # #         self.bidder = True
    # #         remaining_suits = [suit for suit in game.deck.suits if suit != game.table_card.suit]
    # #         game.trump_suit = random.choice(remaining_suits)
    # #         print(f"{self.name} have taken {game.trump_suit} as the trump suit.")



    #    else:  # Redo bidding
    #         if bid == 'take':
    #             self.bidder = True
    #             if not self.human:
    #                 remaining_suits = [suit for suit in game.deck.suits if suit != game.table_card.suit]
    #                 if remaining_suits:  # Ensure there are remaining suits to choose from
    #                     game.trump_suit = random.choice(remaining_suits)
    #                 else:
    #                     remaining_suits = [suit for suit in game.deck.suits]
    #                     game.trump_suit = random.choice(remaining_suits)
    #                 #game.trump_suit = random.choice(remaining_suits)
    #                 print(f"{self.name} have taken {game.trump_suit} as the trump suit.")
    #             else:
    #                 remaining_suits = [suit for suit in game.deck.suits if suit != game.table_card.suit]
    #                 suit_choice = input(f"Choose a suit from {', '.join(remaining_suits)}: ").lower()
    #                 game.trump_suit = suit_choice
    #                 print(f"{self.name} have taken {game.trump_suit} as the trump suit.")


    #    return bid
#/////


    def makes_choice(self, game, trump_choice=None):
        if self.human:
           if game.round == 1 and game.trump_suit is None:
              bid = input("Your turn to bid. Pass or Take? ").lower()
              if bid == 'take':
                self.bidder = True
                remaining_suits = [suit for suit in game.deck.suits]
                suit_choice = input(f"Choose a suit from {', '.join(remaining_suits)}: ").lower()
                game.trump_suit = suit_choice
                print(f"{self.name} have taken {game.trump_suit} as the trump suit.")
              else:
                bid = 'pass'  # Ensure 'pass' is chosen if the human player doesn't take
           else:
               bid = input("Your turn to bid. Pass or Take? ").lower()
        else:
           bid = random.choice(['take', 'pass'])

        print(f"{self.name} chose to {bid}")

        if game.round == 1 and game.trump_suit is not None:
           if bid == 'take':
              self.bidder = True
              game.trump_suit = game.table_card.suit
              print(f"{self.name} have taken {game.trump_suit} as the trump suit.")
        elif game.round == 1 and game.trump_suit is None:
          if bid == 'take':
            self.bidder = True
            game.trump_suit = game.table_card.suit
            print(f"{self.name} have taken {game.trump_suit} as the trump suit.")
        else:  # Redo bidding
          if bid == 'take':
            self.bidder = True
            remaining_suits = [suit for suit in game.deck.suits if suit != trump_choice]
            if remaining_suits:  # Ensure there are remaining suits to choose from
                game.trump_suit = random.choice(remaining_suits)
            else:
                remaining_suits = [suit for suit in game.deck.suits]
                game.trump_suit = random.choice(remaining_suits)
            print(f"{self.name} have taken {game.trump_suit} as the trump suit.")

        return bid







    #    if game.round == 1 :
    #         if bid == 'take':
    #             self.bidder = True
    #             print(f"{self.name} have taken {game.table_card.suit} as the trump suit.")
    #             game.trump_suit = game.table_card.suit



    #    else:  # For redo bidding
    #     if bid == 'take':
    #         self.bidder = True
    #         if not self.human:  # Only if the player is not human, choose a random suit
    #             remaining_suits = [suit for suit in game.deck.suits if suit != game.trump_suit]
    #             game.trump_suit = random.choice(remaining_suits)
    #             print(f"{self.name} have taken {game.trump_suit} as the trump suit.")
    #         else:  # If the player is human, let them choose the suit
    #             remaining_suits = [suit for suit in game.deck.suits if suit != game.trump_suit]
    #             suit_choice = input(f"Choose a suit from {', '.join(remaining_suits)}: ").lower()
    #             game.trump_suit = suit_choice
    #             print(f"{self.name} have taken {game.trump_suit} as the trump suit.")






    # def play_card(self, leading_card, trump_suit):
    #     if self.human:
    #         print(f"{self.name}, it's your turn to play.")
    #         card_index = int(input("Choose a card to play (enter index): "))
    #         return self.hand.cards.pop(card_index)
    #     else:
    #         # Implement bot logic to choose a card to play

    #         return random.choice(self.hand.cards)


    def valid_cards(self, leading_card, trump_suit):
        valid_cards = []




        # Check if the player has a card of the same suit as the leading card
        if leading_card is not None:
           for card in self.hand.cards:
               if card.suit == leading_card.suit:
                  valid_cards.append(card)

        # If the player doesn't have a card of the same suit, check for trump cards
        if not valid_cards and trump_suit:
            for card in self.hand.cards:
                if card.suit == trump_suit:
                    valid_cards.append(card)

        # If the player doesn't have a card of the same suit or a trump card, all cards are valid
        if not valid_cards:
            valid_cards = self.hand.cards

        return valid_cards

    def play_card(self, leading_card, trump_suit,scores):
    # Determine the valid cards the player can play
        played_card = None
        valid_cards = self.valid_cards(leading_card, trump_suit)


    # Check if it's the first card played in the trick
        if leading_card is None:
         # If it's the first card, play a random card if the player is not human
          if not self.human:
               #played_card = random.choice(valid_cards)
               played_card = random.choice(self.hand.cards)
               leading_card = played_card
               return played_card
            #  return random.choice(valid_cards)
          else:
            # If the player is human, prompt them to choose a card
            print("Choose a card to play:")
            for i, card in enumerate(valid_cards):
                print(f"{i + 1}: {card}")
            choice = int(input("Enter the number corresponding to your choice: ")) - 1
            played_card = valid_cards[choice]
            return played_card
            # return valid_cards[choice]
        else:
        # If it's not the first card, follow the rules for playing a card
        # Check if the player has cards of the same suit as the leading card
             same_suit_cards = [card for card in valid_cards if card.suit == leading_card.suit]

        # If the player has cards of the same suit as the leading card, play one of them
             if same_suit_cards:
            # Sort the cards based on their scores in descending order (highest score first)
               #same_suit_cards.sort(key=lambda x: self.SCORES.get(x.rank, 0), reverse=True)
               #same_suit_cards.sort(key=lambda x: self.SCORES.get(x, 0), reverse=True)
               same_suit_cards.sort(key=lambda x: self.SCORES.get(f"{x.suit}_{x.value}", 0), reverse=True)

               played_card = same_suit_cards[0]
               return played_card  # Play the highest scored card of the same suit
             else:
            # Check if the player has any trump cards
                 trump_cards = [card for card in valid_cards if card.suit == trump_suit]

            # If the player has trump cards, play one of them
                 if trump_cards:
                # Sort the trump cards based on their scores in descending order (highest score first)
                    #trump_cards.sort(key=lambda x: self.SCORES.get(x.rank, 0), reverse=True)
                    #trump_cards.sort(key=lambda x: self.SCORES.get(x, 0), reverse=True)
                    same_suit_cards.sort(key=lambda x: self.SCORES.get(f"{x.suit}_{x.value}", 0), reverse=True)

                    played_card = trump_cards[0]
                    return played_card  # Play the highest scored trump card
                 else:

                # If the player doesn't have cards of the same suit or trump cards, play any card
                  played_card = valid_cards[0]
                  #self.hand.remove_card(played_card,self.hand)
                  return played_card

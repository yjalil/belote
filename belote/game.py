import random
from belote.card import Card
from belote.hand import Hand
from belote.player import Player
from belote.deck import Deck

class BeloteGame:
    def __init__(self):
        self.table_card = None
        self.trump_suit = None
        self.human_player = Player('Human', human = True)
        self.players = [self.human_player, Player('Computer_1'), Player('Computer_2'),Player('Computer_3')]
        random.shuffle(self.players)
        self.hand_size = 5
        self.deck = Deck()
        self.round = 0
        self.gameover = False

    def show_me_table(self,card_str):
        self.table_card = self.deck.pick_card(card_str)
        print('---------Table card picked -----------')
        print(str(self.table_card))
        return self



    def show_me_human_hand(self, cards_str):
        self.human_player.hand = Hand([str(self.deck.pick_card(card)) for card in cards_str])

        print('---------Human cards picked -----------')
        for card in self.human_player.hand.cards:
            card.update_score(self.trump_suit)
            print(f"{card} - Score: {card.score}")

        return self

    def first_dealing(self):
        for player in self.players:
            if not player.human:
                player.hand = Hand([str(self.deck.pick_card()) for i in range(self.hand_size)])
                print('---------Bot cards picked -----------')
                for card in player.hand.cards:
                    card.update_score(self.trump_suit)
                    print(f"{card} - Score: {card.score}")

        return self


    # def bidding_round(self):
    #     self.round += 1
    #     bids = []
    #     for player in self.players:
    #         print(f'------Round {self.round} : {player.name} to play-------')
    #         bids.append(player.makes_choice(self))
    #         if bids[-1] == 'take':
    #         #    print(f"{player.name} have taken {self.trump_suit} as the trump suit.")
    #            print(f"Round {self.round} is over.")
    #         for player in self.players:
    #             print(f'{player.name} bid: {bids[-1]}')
    #             print(f'All pass: {all_pass}')

    #             return self.gameover

    #     all_pass = all(bid == 'pass' for bid in bids)
    #     if all_pass:
    #        print(f"All players passed. Redoing the bidding round...")
    #        self.trump_suit = None
    #        bids = []
    #        for player in self.players:
    #            print(f'------Round {self.round} : {player.name} to play-------')
    #            bids.append(player.makes_choice(self))
    #            if player.human:
    #               if bids[-1] == 'take':
    #                   remaining_suits = [suit for suit in self.deck.suits if suit != self.trump_suit]
    #                   suit_choice = input(f"Choose a suit from {', '.join(remaining_suits)}: ").lower()
    #                   self.trump_suit = suit_choice
    #                 #   print(f"{player.name} have taken {self.trump_suit} as the trump suit.")
    #                   break

    #            else:
    #                  if bids[-1] == 'take':
    #                    remaining_suits = [suit for suit in self.deck.suits if suit != self.trump_suit]
    #                    self.trump_suit = random.choice(remaining_suits)
    #                 #    print(f"{player.name} have taken {self.trump_suit} as the trump suit.")
    #                    break


    #     return self.gameover




    # def bidding_round(self):
    #      self.round += 1
    #      bids = []

    #      for player in self.players:
    #          print(f'------Round {self.round} : {player.name} to play-------')
    #          bids.append(player.makes_choice(self))
    #          if bids[-1] == 'take':
    #             print(f"Round {self.round} is over.")

    #             return self.gameover


    #      for player in self.players:
    #         print(f'{player.name} bid: {bids[-1]}')

    #      all_pass = all(bid == 'pass' for bid in bids)
    #      print(f'All pass: {all_pass}')

    #      if all_pass:
    #         print(f"All players passed. Redoing the bidding round...")
    #         self.trump_suit = None
    #         bids = []
    #         for player in self.players:
    #             print(f'------Round {self.round} : {player.name} to play-------')
    #             bids.append(player.makes_choice(self))
    #             if player.human:
    #                if bids[-1] == 'take':
    #                  remaining_suits = [suit for suit in self.deck.suits if suit != self.trump_suit]
    #                  suit_choice = input(f"Choose a suit from {', '.join(remaining_suits)}: ").lower()
    #                  self.trump_suit = suit_choice
    #                 #   print(f"{player.name} have taken {self.trump_suit} as the trump suit.")
    #                  break
    #             else:
    #               if bids[-1] == 'take':
    #                 remaining_suits = [suit for suit in self.deck.suits if suit != self.trump_suit]
    #                 self.trump_suit = random.choice(remaining_suits)
    #                 #    print(f"{player.name} have taken {self.trump_suit} as the trump suit.")
    #                 break

    #      return self.gameover


    # def bidding_round(self):
    #      all_pass_second_round = False
    #      self.round += 1
    #     #  took_bid = False
    #      bids = []

    #      for player in self.players:
    #           print(f'------Round {self.round} : {player.name} to play-------')
    #           bids.append(player.makes_choice(self))
    #           if bids[-1] == 'take':
    #              print(f"Round {self.round} is over.")
    #              self.second_dealing()
    #              took_bid = True
    #              return
    #              #return self.gameover
    #              #break
    #      print("Bids:", bids)
    #     #  for player in self.players:
    #     #      print(f'{player.name} bid: {bids[-1]}')

    #      all_pass = all(bid == 'pass' for bid in bids)
    #      print(f'All pass: {all_pass}')

    #      if all_pass:
    #          print(f"All players passed. Redoing the bidding round...")
    #          self.trump_suit = None
    #          bids = []

    #          #self.bidding_round()  # Call the bidding round again to start over
    #          #return self.gameover
    #          for player in self.players:
    #              print(f'------Round {self.round} : {player.name} to play-------')
    #              bids.append(player.makes_choice(self))
    #              if player.human:
    #                 if bids[-1] == 'take':
    #                   remaining_suits = [suit for suit in self.deck.suits if suit != self.trump_suit]
    #                   suit_choice = input(f"Choose a suit from {', '.join(remaining_suits)}: ").lower()
    #                   self.trump_suit = suit_choice
    #                   print(f"{player.name} have taken {self.trump_suit} as the trump suit.")
    #                   break
    #              else:
    #                if bids[-1] == 'take':
    #                  remaining_suits = [suit for suit in self.deck.suits if suit != self.trump_suit]
    #                  self.trump_suit = random.choice(remaining_suits)
    #                  print(f"{player.name} have taken {self.trump_suit} as the trump suit.")
    #                  self.second_dealing()
    #                  return
    #                 #  break


    #              all_pass_second_round = all(bid == 'pass' for bid in bids)
    #              print(f'All pass in second round: {all_pass_second_round}')

    #              if all_pass_second_round:
    #                  print(f"All players passed again. Game over.")
    #                  return


    #     #  if took_bid:
    #     #      self.second_dealing()



    #      return self.gameover

    #****






    def bidding_round(self):
        all_pass_second_round = False
        self.round += 1
        trump_choice = None

        bids = []

        for player in self.players:
            print(f'------Round {self.round} : {player.name} to play-------')
            #choice = player.makes_choice(self)
            choice = player.makes_choice(self)
            if isinstance(choice, tuple):  # Check if the choice is a tuple
                bid, trump_choice = choice
            else:
                bid = choice
                trump_choice = None
            bids.append(bid)
            if bid == 'take':
                print(f"Round {self.round} is over.")
                self.second_dealing()
                leader_index = self.players.index(player)  # Get the index of the player who took the bid
                self.play_tricks(leader_index, self.trump_suit)
                return

        print("Bids:", bids)

        all_pass = all(bid == 'pass' for bid in bids)
        print(f'All pass: {all_pass}')

        if all_pass:
            print(f"All players passed. Redoing the bidding round...")
            self.trump_suit = None
            bids = []

            for player in self.players:
                print(f'------Round {self.round} : {player.name} to play-------')
                choice = player.makes_choice(self)
                if isinstance(choice, tuple):  # Check if the choice is a tuple
                    bid, trump_choice = choice
                else:
                    bid = choice
                    trump_choice = None
                bids.append(bid)
                if bid == 'take':
                    print(f"Round {self.round} is over.")
                    self.second_dealing()
                    leader_index = self.players.index(player)  # Get the index of the player who took the bid
                    self.play_tricks(leader_index, self.trump_suit)
                    return

                # if not player.human and bid == 'take':
                #     remaining_suits = [suit for suit in self.deck.suits if suit != trump_choice]
                #     self.trump_suit = random.choice(remaining_suits)
                #     print(f"{player.name} have taken {self.trump_suit} as the trump suit.")
                #     break


                # if player.human and bid == 'take':
                #     remaining_suits = [suit for suit in self.deck.suits if suit != trump_choice]
                #     suit_choice = input(f"Choose a suit from {', '.join(remaining_suits)}: ").lower()
                #     self.trump_suit = suit_choice
                #     print(f"{player.name} have taken {self.trump_suit} as the trump suit.")
                #     break

                if player.human and bid == 'take':
                 remaining_suits = [suit for suit in self.deck.suits if suit != trump_choice]
                 suit_choice = input(f"Choose a suit from {', '.join(remaining_suits)}: ").lower()
                 self.trump_suit = suit_choice
                 print(f"{player.name} have taken {self.trump_suit} as the trump suit.")
                 break


                elif not player.human and bid == 'take':
                    remaining_suits = [suit for suit in self.deck.suits if suit != trump_choice]
                    self.trump_suit = random.choice(remaining_suits)
                    print(f"{player.name} have taken {self.trump_suit} as the trump suit.")
                    break


            all_pass_second_round = all(bid == 'pass' for bid in bids)
            print(f'All pass in second round: {all_pass_second_round}')

            if all_pass_second_round:
                print(f"All players passed again. Game over.")
                return






    def second_dealing(self):
        print("Starting second dealing...")
        print("Table card:", self.table_card)
        for player in self.players:
            if player.bidder:
               for i in range(2):
                   player.hand.add_card(str(self.deck.pick_card()))
               player.hand.add_card(str(self.table_card))
               #player.hand.add_card(self.table_card)
               self.table_card = None
            else:
                 for i in range(3):
                    player.hand.add_card(str(self.deck.pick_card()))

        for player in self.players:
            print(f"Hand of {player.name}: {player.hand}")

        print("Second dealing completed.")

        return self




    # def play_trick(players, trick_winner_index, trump_suit):
    #     leading_card = None
    #     trick_winner_index = trick_winner_index
    #     current_player_index = trick_winner_index

    #     for _ in range(len(players[0].hand) - 1):
    #          current_player = players[current_player_index]
    #          played_card = current_player.play_card(leading_card, trump_suit)

    #          if leading_card is None:
    #            leading_card = played_card

    #          if played_card.beats(leading_card, trump_suit):
    #             trick_winner_index = current_player_index
    #             leading_card = played_card

    #          current_player_index = (current_player_index + 1) % len(players)

    #          trick_winner = players[trick_winner_index]
    #          trick_winner.add_trick(leading_card)

    #     return trick_winner_index



    # def calculate_scores(self):
    #     for player in self.players:
    #         player_score = 0
    #         for card in player.collected_cards:
    #             card_score = self.SCORES.get(card.rank, 0)
    #             player_score += card_score
    #         print(f"{player.name} score:", player_score)


    def calculate_scores(self):
       for player in self.players:
           player_score = 0
           for card in player.collected_cards:

              card_score = Card.SCORES.get(card.value, 0)
              player_score += card_score
            #   card_score = Card.SCORES.get(card.value, 0)
            #   player_score += card_score
           print(f"{player.name} score:", player_score)


    # def play_tricks(self, leader_index, trump_suit):
    # # Initialize variables

    #     current_player_index = leader_index
    #     trick_winner_index = leader_index
    #     tricks = [[] for _ in range(len(self.players))]  # Store cards played in each trick
    #     print("Starting tricks...")

    # # Iterate over tricks until all cards have been played
    #     for _ in range(len(self.players[0].hand)):
    #        leading_card = None  # Leading card of the trick
    #        print("New trick started.")

    #     # Iterate over players in clockwise order starting with the leader
    #        for _ in range(len(self.players)):
    #            current_player = self.players[current_player_index]
    #            played_card = current_player.play_card(leading_card, trump_suit)
    #            print(f"{current_player.name} played {played_card}.")

    #            tricks[current_player_index].append(played_card)

    #         # Ensure leading card is set for the trick
    #            if leading_card is None:
    #               leading_card = played_card
    #               print(f"Leading card set to {leading_card}.")

    #            elif played_card.beats(leading_card, trump_suit):
    #             leading_card = played_card
    #             trick_winner_index = current_player_index


    #         # Add played card to the current trick
    #            #tricks[current_player_index].append(played_card)

    #         # Update leading card if necessary
    #         #    if leading_card is not None and played_card.beats(leading_card, trump_suit):
    #         #       leading_card = played_card
    #         #       trick_winner_index = current_player_index

    #         # Move to the next player
    #            current_player_index = (current_player_index + 1) % len(self.players)

    #     # Determine winner of the trick
    #        trick_winner = self.players[trick_winner_index]
    #        print(f"Trick winner: {trick_winner.name}")

    #     # Collect cards from the trick
    #        for trick_cards in tricks:
    #           trick_winner.collect_cards(trick_cards)

    #     # Reset variables for the next trick
    #        current_player_index = trick_winner_index
    #        trick_winner_index = trick_winner_index
    #        tricks = [[] for _ in range(len(self.players))]

    # # Calculate scores after all tricks have been played
    #     self.calculate_scores()

#***

    # def play_tricks(self, leader_index, trump_suit):
    # # Initialize variables
    #    current_player_index = leader_index
    #    trick_winner_index = leader_index
    #    tricks = [[] for _ in range(len(self.players))]  # Store cards played in each trick
    #    print("Starting tricks...")

    #    leading_card = None
    # # Iterate over tricks until all cards have been played
    #    for _ in range(len(self.players[0].hand)):
    #         # Leading card of the trick
    #       print("New trick started.")

    #     # Ask the leader player to choose a card of their choice
    #       leader_player = self.players[current_player_index]
    #       if leader_player.human:
    #          print(f"{leader_player.name}, choose a card to play:")
    #          print(leader_player.hand)
    #          chosen_card_index = int(input("Enter the index of the card you want to play: "))
    #          played_card = leader_player.hand.cards[chosen_card_index]
    #       else:
    #          played_card = leader_player.play_card(leading_card, trump_suit, Card.SCORES)

    #       print(f"{leader_player.name} played {played_card}.")
    #       tricks[current_player_index].append(played_card)

    #     # Ensure leading card is set for the trick
    #       if leading_card is None:
    #          leading_card = played_card
    #          print(f"Leading card set to {leading_card}.")

    #       elif played_card.beats(leading_card, trump_suit):
    #          leading_card = played_card
    #          trick_winner_index = current_player_index


    #       leader_player.hand.remove_card(played_card)
    #     # Move to the next player
    #       current_player_index = (current_player_index + 1) % len(self.players)

    #     # Continue playing cards in clockwise order
    #       while current_player_index != leader_index:
    #          current_player = self.players[current_player_index]
    #          played_card = current_player.play_card(leading_card, trump_suit,Card.SCORES)
    #          print(f"{current_player.name} played {played_card}.")
    #          tricks[current_player_index].append(played_card)

    #         # Update leading card if necessary
    #          if played_card.beats(leading_card, trump_suit):
    #              leading_card = played_card
    #              trick_winner_index = current_player_index

    #          current_player.hand.remove_card(played_card)
    #         # Move to the next player
    #          current_player_index = (current_player_index + 1) % len(self.players)

    #     # Determine winner of the trick
    #          trick_winner = self.players[trick_winner_index]
    #          print(f"Trick winner: {trick_winner.name}")

    #     # Collect cards from the trick
    #       #for trick_cards in tricks:
    #          #trick_winner.collect_cards([(player, played_card,current_player_index) for player, played_card in zip(self.players, tricks[current_player_index])])
    #          #trick_winner.collect_cards(trick_cards)
    #          #trick_winner.collect_cards([(player, played_card, current_player_index) for player, played_card in zip(self.players, tricks[current_player_index])], current_player_index)
    #          #trick_winner.collect_cards([(player, played_card) for player, played_card in zip(self.players, tricks[current_player_index])])
    #          #trick_winner.collect_cards(trick_cards)
    #          # Collect cards from the trick

    #          #trick_winner.collect_cards([(player, played_card) for player, played_card in zip(self.players, trick_cards)])




    #     # Reset variables for the next trick
    #    current_player_index = trick_winner_index
    #    trick_winner_index = trick_winner_index
    #    tricks = [[] for _ in range(len(self.players))]

    # # Calculate scores after all tricks have been played
    #    self.calculate_scores()


    def play_tricks(self, leader_index, trump_suit):
    # Initialize variables
       current_player_index = leader_index
       trick_winner_index = leader_index
       tricks = [[] for _ in range(len(self.players))]  # Store cards played in each trick
       print("Starting tricks...")

       leading_card = None

    # Continue playing until all cards have been played
       while any(self.players[i].hand.cards for i in range(len(self.players))):
          print("New trick started.")

        # Play cards for each player
          for i in range(len(self.players)):
              current_player = self.players[current_player_index]
              played_card = current_player.play_card(leading_card, trump_suit, Card.SCORES)
              print(f"{current_player.name} played {played_card}.")
              tricks[current_player_index].append(played_card)

            # Update leading card if necessary
              if leading_card is None or played_card.beats(leading_card, trump_suit):
                 leading_card = played_card
                 trick_winner_index = current_player_index

            # Remove the played card from the player's hand
              current_player.hand.remove_card(played_card)

            # Move to the next player
              current_player_index = (current_player_index + 1) % len(self.players)

        # Determine the winner of the trick
          trick_winner = self.players[trick_winner_index]
          print(f"Trick winner: {trick_winner.name}")

        # Set the next leader to be the winner of this trick
          current_player_index = trick_winner_index

        # Reset the leading card for the next trick
          leading_card = None

        # Reset the trick winner index
          trick_winner_index = current_player_index

        # Reset the tricks list for the next trick
          tricks = [[] for _ in range(len(self.players))]

    # Calculate scores after all tricks have been played
       self.calculate_scores()




    def determine_trick_winner(self, trick_cards):
        lead_suit = trick_cards[0][1].suit
        trump_cards = [(player, card) for player, card in trick_cards if card.suit == self.trump_suit]

        # If trump cards are played, determine the winner among trump cards
        if trump_cards:
            winning_card = max(trump_cards, key=lambda x: x[1].score)[1]
            winning_player = [player for player, card in trick_cards if card == winning_card][0]
        else:
            lead_cards = [(player, card) for player, card in trick_cards if card.suit == lead_suit]
            winning_card = max(lead_cards, key=lambda x: x[1].score)[1]
            winning_player = [player for player, card in trick_cards if card == winning_card][0]

        return winning_player, winning_card

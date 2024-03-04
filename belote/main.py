from belote.game import BeloteGame
from belote.card import Card
from belote.player import Player

if __name__ == '__main__':
    game = BeloteGame()
    #player = Player()
    game.show_me_table('chbada_4')
    game.show_me_human_hand(['copas_sota','dheb_4','k7el_las','copas_las','chbada_dix'])
    game.first_dealing()
    game.bidding_round()
    game.play_tricks()
    #leader_index, trump_suit = game.bidding_round()
    #player.play_card(leading_card, trump_suit)

    #if leader_index is not None and trump_suit is not None:
       #game.play_tricks(leader_index, trump_suit)
    #print("Table card:", game.table_card)
    #game.second_dealing(game.table_card)
    #game.second_dealing()
    # card = Card('dheb_neuf')
    # trump_suit = 'dheb'
    # print(card.update_score(trump_suit=trump_suit))

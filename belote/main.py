from belote.game import BeloteGame
from belote.card import Card

if __name__ == '__main__':
    game = BeloteGame()
    game.show_me_table('chbada_4')
    game.show_me_human_hand(['copas_sota','dheb_4','k7el_las','copas_las','chbada_dix'])
    game.first_dealing()
    game.bidding_round()
    game.second_dealing()
    # card = Card('dheb_neuf')
    # trump_suit = 'dheb'
    # print(card.update_score(trump_suit=trump_suit))

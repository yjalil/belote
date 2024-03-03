from belote.game.game import BeloteGame


if __name__ == '__main__':
    game = BeloteGame()
    game.show_me_table('chbada_4')
    game.show_me_human_hand(['copas_sota','dheb_4','k7el_las','copas_las','chbada_dix'])
    game.first_dealing()
    game.bidding_round()
    game.second_dealing()

from deck import deck


discard_pile = deck()
draw_pile = deck(True)

draw_pile.fan()

discard_pile.fan()


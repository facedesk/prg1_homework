'''
#suit
#rank
'''
from rank import rank
from suit import suit

class card():
    def __init__(self,parameter_suit,parameter_rank):
        r = rank()
        valid_rank = r.validate(parameter_rank)

        s = suit()
        valid_suit = s.validate(parameter_suit)

        if(valid_rank and valid_suit):
            self.suit = parameter_rank
            self.rank = parameter_rank
        else:
            self.suit = "Invalid"
            self.rank = "Invalid"
    def display(self):
        print(self.rank + " of " + self.suit)

card1 = card("hearts","11")
card1.display()
card2 = card("lionking","5")
card2.display()
card3 = card("5","9")
card3.display()
card4 = card("spades","ace")
card4.display()
card5 = card("ace","spades")
card5.display()
card6 = card("clubs","6")

card7 = card("hearts","10")

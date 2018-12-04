class suit():
    def __init__(self):
        self.values = {
            "hearts":0,
            "spades":1,
            "diamonds":2,
            "clubs":3
        }
    def validate(self, suit_value):
        if(suit_value in self.values):
            return True
        else:
            return False


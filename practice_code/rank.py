'''
number or face value

#dictionary of legit values
#face_value
'''
class rank():
    def __init__(self):
        self.values = {
            "ace":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9,
            "10":10,
            "jack":11,
            "queen":12,
            "king":13
        }
    def validate(self, face_value):
        #return false if it is not in values
        #return true if it is
        if(face_value in self.values):
            return True
        else:
            return False

        
        

    
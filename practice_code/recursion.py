'''
recursively count up to 10

'''

def countup(x=0):
    print(x)
    if(x==10):
        return
    else:
        return countup(x+1)

#countup()
'''

recurisvely count down from 10 to 0
'''
def countdown(x=10):
    print(x)
    if(x==0):
        return
    else:
        return countdown(x-1)
countdown()
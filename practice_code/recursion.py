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


'''
We have bunnies standing in a line, 
numbered 1, 2, ... The odd bunnies (1, 3, ..)
 have the normal 2 ears. The even bunnies 
 (2, 4, ..) we'll say have 3 ears, because 
 they each have a raised foot. Recursively 
 return the number of "ears" in the 
 bunny line 1, 2, ... n (without loops or 
 multiplication).
'''
def simple_bunny_ears(bunnies):
    if(bunnies == 0):
        return 0
    else:
        return 2 + simple_bunny_ears(bunnies -1)    


def odd_bunny_ears(bunnies):
    if(bunnies == 0):
        return 0
    elif(bunnies %2 == 0):
        return 2 + odd_bunny_ears(bunnies -1)
    else:
        return 1 + odd_bunny_ears(bunnies -1)


'''
towers of hanoi
'''
def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

moveTower(3,"A","B","C")
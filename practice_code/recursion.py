def countup(count=0):
    if(count>10):
        return
    else:
        print(count)
        return countup(count + 1)
    pass

countup()

def countdown(count=10):
    if(count < 1):
        return
    else:
        print(count)
        return countdown(count -1)
    pass

countdown()

'''
there is a field of bunnies, and each bunny has two ears
write a program that can count ears given bunnies 
using recursion
'''

def simple_bunny_ears(bunnies):
    if(bunnies == 0):
        return 0
    else:
        return 2 + simple_bunny_ears(bunnies -1)
print(simple_bunny_ears(5))

'''
there is a field of bunnies, and every other bunny has two ears,
the bunnies inbetween raise a foot for a third ear
write a program that can count ears given bunnies 
using recursion
'''
def complex_bunny_ears(bunnies):
    if(bunnies ==0 ):
        return 0
    elif(bunnies % 2 == 0):
        return 2 + complex_bunny_ears(bunnies -1)
    else:
        return 3 + complex_bunny_ears(bunnies - 1)
    
print(complex_bunny_ears(5))



import random

def inorder(items):
    count = 0
    for item in items:
        if(count+1 < len(items)):
            if items[count+1] < item:
                return False
        count +=1
    return True


def shuffle(items):
    random.shuffle(items)
    return items


def bogo(x):
    while not inorder(x):
        shuffle(x)
        print(x)
    return x
 
values = [1,4,53,3,5,6,7,3,4,1,5,6,3,26,53,3,5,4,3,34,5,3,1]
values = bogo(values)
print(values)
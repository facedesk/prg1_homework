#[4,2,1,6,3,2,5]
#[4,2,1] [6,3,2,5]
def order(left,right,total):
    leftsize= len(left)
    rightsize = len(right)
    if(leftsize ==0 and rightsize == 0):
        return total
    elif(leftsize ==0):
        return total+right
    elif(rightsize ==0):
        return total+left
    else:
        if(left[0]>right[0]):
            total.append(right[0])
            right.pop(0)
        else:
            total.append(left[0])
            left.pop(0)
        return order(left,right,total)

def merge(items):
    if(len(items) <= 1):
        return items
    
    
    else:
        half = int(len(items)/2)
        items_left= items[:half]
        items_right=items[half:]
        
        left = merge(items_left)
        right = merge(items_right)
        x = order(left,right,[])
        return x

print(merge([1,3,5,2]))

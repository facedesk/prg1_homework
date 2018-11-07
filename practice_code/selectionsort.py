'''
selection sort:
find the minimum value and swap it with the value you are on
'''
def find_minimum_value(values):
    '''
    find the smallest value in a given list
    '''
    special_value = values[0]
    for value in values:
        if(value < special_value):
            special_value = value
    return special_value

def find_position(values,element):
    #return the integer position where the element is found
    index = 0
    for value in values:
        if(value == element):
            return index
        index +=1
    pass

def selection_sort(values):

    count = 0
    while(count < len(values)):
        smallest_value = find_minimum_value(values[count:])
        position = find_position(values,smallest_value)
        values[position] = values[count]
        values[count] = smallest_value
        count +=1
    return values

unsorted = [243,8,7,-10,5,2,3,4,1]
print(selection_sort(unsorted))


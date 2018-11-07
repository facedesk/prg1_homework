'''
insertion sort:
find the minimum value
remove that from the list
add that to a new list
return that list
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
def insertion_sort(values):
    smallest_list= []
    while(len(values)>0):  
        smallest = find_minimum_value(values)
        values.remove(smallest)
        smallest_list.append(smallest)
        print(smallest_list)
    return smallest_list
    #find min value
    #remove that
    #add to new list


#test 4 values
unsorted = [5,3,6,54]
sorted = insertion_sort(unsorted)
print(sorted)
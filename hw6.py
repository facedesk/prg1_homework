'''
For this homework, your code must match the area called specs.
This means you must use the correct function names, correct parameter names,
and fulful the function needs.


Good luck and happy sorting!
'''


'''
Problem 1
Create a function called swap.
This function will take in as parameters two variables a, and b. 
It will then replace a and b

specs:
function name: swap
description: replace a with b and be with a
parameters: a  and b
returns: a and b


pseudo code:
swap a,b:
    set temp to a
    set a to b
    set b to temp
    return a,b

x = 10
y = 30
swap x,y

print(x,y)
30 10
'''



'''
Problem 2
Create a function called bubble
this function will take in as a parameter a list called items
it will loop through the list using a while loop and swap using the function 
(from problem 1) the first two values that are out of order and return false
If no two items are out of order, then return true 


specs:
function name: bubble
description: 
parameters: items
returns: True or False


pseudo code:

bubble list
    set itemFound to false
    set index = 0
    while not itemFound and index is less than the length of list:
        if index -1 > 0 and item at index-1 > item at index:
            swap item at index-1,item at index
        increase index by one
'''



'''
Problem 3
Create a function called bubble_sort that takes in as a parameter a list called items
it will continue to loop and call bubble until all items are successfully placed in order

specs:
function name: bubble_sort
description: perform the algorithm bubble sort using the functions from problem 1 and 2
parameters: items
returns: nothing


'''
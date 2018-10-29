
#Ask the user how many times they want to count
#Change the code to count to that value

#display a square that is length & height of that number of times
'''
first display a line with that number of stars

****

display a square with the number of stars

****
****
****
****

***
***
***

'''

times = int(input('how many times would you like to loop'))

y = 0
while(y <times):
    stars = ""
    x = 0
    while(x < times):
        stars += "*"
        x=x+1
    print(stars)
    y+=1

'''
write a function that will tell you if a number is in range of two other numbers
'''

def number_in_range(low,high,number):
    return low < number and high > number:
     
number1 = 1
number10=10
number_in_the_range= 4
number_out_range = -5
number_too_high = 100

isnumber1inrange = number_in_range(number1,number10,number_in_the_range)
print(isnumber1inrange)

number_in_range(number1,number10,number_out_range)

number_in_range(number1,number10,number_too_high)



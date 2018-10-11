'''
a strong number is defined as a number that has the sum of the factorial of
each digit is equal to its original number

'''
print("please enter a number that might be strong")
snumber = input(">")

#get all of the digits (split)
digits = list(snumber)

sum = []
#calculate factorial for each digit
for digit in digits:
    factorial = 1
    for number in range(1,int(digit)+1):
        factorial = number * factorial
    print(factorial)
    sum.append(factorial)


#add all factorials together
final_factorial = 0
for number in sum:
    final_factorial += number
print(final_factorial)
#check if the sum is same as original

if(final_factorial ==  snumber):
    print(snumber,"This number is strong")
    




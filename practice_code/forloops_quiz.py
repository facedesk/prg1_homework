# ask user for input
#split the input on a space to get a list of strings
#loop through each value turning the string into an int
#create a variable to store the sum before the loop
#inside the loop add the sum with each integer from the list
#outside of the loop display the sum




numbers = input("Enter numbers seperated by a space")
numbers_list = numbers.split(" ")
print("done")

max_number = int(numbers_list[0])
for number in numbers_list:
    inumber = int(number)
    if(max_number < inumber):
        max_number = inumber
print("the largest number is ",max_number)



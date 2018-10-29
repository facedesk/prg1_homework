number = input("Please enter a number: ")
number = int(number)

#right datatype - int


sum = 0
#variable for sum!!!

for count in range(number+1):
    if(count%7 != 0):
        sum = sum + count

print(sum)
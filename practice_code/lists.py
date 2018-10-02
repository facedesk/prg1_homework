numbers = input("enter 10 numbers with a comma inbetween")



print(numbers)
numbers_list = numbers.split("comma")
numbers_count = len(numbers_list)
half = int(numbers_count/2)

print(numbers_list)
last_half = numbers_list[half:numbers_count]
print(last_half)
first_half = numbers_list[0:half]
print(first_half)

print(numbers_list[1:numbers_count-1])

print(numbers_list[::-1])

reverse_numbers = ",".join(numbers_list[0:numbers_count:-1])
print(reverse_numbers)


'''
import matplotlib.pyplot as plt

xlist=[0,1,2]
ylist=[1,2,4]
x=[1,2,3,4,5]
y=[1,4,9,16,25]

plt.title("y=x**2")
plt.plot(x,y)
plt.show()
input("press enter")
'''


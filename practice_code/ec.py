snumbers = input("enter numbers seperate by a space")

lnumbers = snumbers.split(" ")

largest_neighbor_distance = int(lnumbers[0])
largest_neighbor_distance_sum = int(lnumbers[0])
count = 0

for sn in lnumbers:
    lag = 0
    current = int(sn)
    next = 0
    if(count !=0):
        lag = int(lnumbers[count-1])
    if(count != len(lnumbers)-1):
        next = int(lnumbers[count+1])

    lag_distance = current - lag
    if(lag_distance <0 ):
        lag_distance = lag - current

    next_distance = current - next
    if(next_distance <0 ):
        next_distance = next - current

    sum = lag_distance + next_distance
    if(sum > largest_neighbor_distance_sum):
        largest_neighbor_distance_sum = sum
        largest_neighbor_distance = int(sn)

    count +=1
print(largest_neighbor_distance)
print(largest_neighbor_distance_sum)

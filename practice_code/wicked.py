print("please enter 5 numbers seperated by a space")
strumbers = input(">")
numbers = strumbers.split(" ")
if(len(numbers)==5):
    sum = 0
    for sx in numbers:
        x = float(sx)
        sum +=x

    print(sum," is not your final score")

    score = 0
    for swicked in numbers:
        wicked = float(swicked)
        if(wicked == 13.0):
            score += -100
        elif(wicked == 7.0):
            score += 30
        elif(wicked %2 == 1):
            score += wicked * 2
        elif(wicked %2 == 0):
            score += wicked/2
        else:
            print("not valid")
        
    print(score, " is your final score")
else:
    print("enter the correct numbers please try again")

#1
nicknames = {"Jack Newbaur": "Squi","Lauren Laplour":"Apple"}

#2
nicknames["Alphonse Elric"] = "Tin Man"
nicknames["Edward Elric"] = "Metal Arm"
nicknames["James Jones"] = "Vader"


description = ""
#3
for name in nicknames:
    description += name + " goes by the name " + nicknames[name] + ", "
#4
print(description)
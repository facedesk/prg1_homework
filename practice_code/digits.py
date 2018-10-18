import matplotlib.pyplot as plt
from itertools import groupby



xcoords= [2**i for i in range(50)]
ycoords = list(map(lambda x: len(str(x)), xcoords))

counts = [len(list(group)) for key, group in groupby(ycoords)]


plt.title("Digits versus exponent of binary numbers")
plt.scatter(xcoords,ycoords)
plt.show()
input()



import sys
import os
import time
colors = {
    "black":0,
    "blue":1,
    "green":2
}
'''
    0 = Black       8 = Gray
    1 = Blue        9 = Light Blue
    2 = Green       A = Light Green
    3 = Aqua        B = Light Aqua
    4 = Red         C = Light Red
    5 = Purple      D = Light Purple
    6 = Yellow      E = Light Yellow
    7 = White       F = Bright White
'''

# Normal colours for a Command Prompt from CMD.EXE is white on black.
os.system("COLOR 0"+ str(colors["blue"]))
print("\nNormal Command Prompt default colours, white on black...\n")
time.sleep(1)
os.system("COLOR 0"+ str(colors["green"]))
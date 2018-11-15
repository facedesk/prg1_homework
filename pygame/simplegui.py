
import math
import random
import time
import simpleguitk as simplegu

# Global Variables

canvas_width = 600
canvas_height = 600

# Event Handlers
def draw(canvas):
    # Line Segment
    point_one = (10, 20)
    point_two = (300, 20)
    line_width = 5
    line_color = "Red"
    canvas.draw_line(point_one, point_two, line_width, line_color)
    
    
# Frame

frame = simplegui.create_frame("Shapes", canvas_width, canvas_height) 

# Register Event Handlers

frame.set_draw_handler(draw)

# Remember to start the frame
frame.start()
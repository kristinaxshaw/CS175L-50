#Kristina Shaw
#Turtle_Graphics_Stop_Sign.py
#CS-175L

#importing math and turtle
import math
import turtle

#Declaring variables
window_width = 400
window_height = 400
animation_speed = 0
num_sides = 8
length = 100
angle = 45
text_x = -5
text_y = -1

#setting the first fill color, which makes the background of the stop sign red   
turtle.color("black", "red")

#setting the location of the start of the drawing
turtle.penup()
turtle.goto(-50,145)
turtle.pendown()
turtle.begin_fill()

#drawing the octagon
for x in range(8):
    turtle.forward(100)
    turtle.right(45)
turtle.end_fill()

#changing thecolor to white to write the word 'stop'
turtle.color('White')

#setting the location of the writing
turtle.penup()
turtle.goto(0,0)

#command to write along with the font type, size, and alignment
turtle.write('Stop', align = 'center', font=('Arial', 40, 'bold'))

#end of program
turtle.done()




    

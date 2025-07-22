!pip install ColabTurtle

from ColabTurtle.Turtle import *
initializeTurtle()
speed(4)

# Draw a 5-pointed star
for _ in range(5):
    forward(150)
    right(144)

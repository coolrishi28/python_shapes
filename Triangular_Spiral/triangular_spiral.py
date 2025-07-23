!pip install ColabTurtle

from ColabTurtle.Turtle import *

initializeTurtle()
speed(7)

distance = 10
for _ in range(40):
    forward(distance)
    left(120)
    distance += 10

!pip install ColabTurtle

from ColabTurtle.Turtle import *

initializeTurtle()
speed(8)  # Make it faster

# Draw a circular spiral
distance = 5  # Starting distance

for _ in range(50):  # Number of turns
    forward(distance)
    left(30)           # Adjust angle for spiral tightness
    distance += 2     # Gradually increase distance

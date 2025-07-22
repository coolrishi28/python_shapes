!pip install ColabTurtle

from ColabTurtle.Turtle import *

initializeTurtle()
speed(6)  # Make it faster

# Draw a square spiral
distance = 5  # Starting distance

for _ in range(50):  # Number of turns
    forward(distance)
    left(90)           # Adjust angle for spiral tightness
    distance += 8      # Gradually increase distance

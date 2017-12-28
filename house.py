import turtle
import math
turtle.shape("turtle")
tilt = 45
rightangle = 90
length = 100
diagonal = math.sqrt(length**2 + length**2)

turtle.forward(length)
turtle.left(rightangle)
turtle.forward(length)
turtle.left(rightangle)
turtle.forward(length)
turtle.left(rightangle)
turtle.forward(length)
turtle.left(rightangle)

turtle.left(tilt)
turtle.forward(diagonal)
turtle.left(rightangle)
turtle.forward(diagonal/2)
turtle.left(rightangle)
turtle.forward(diagonal/2)
turtle.left(rightangle)
turtle.forward(diagonal)

turtle.exitonclick()

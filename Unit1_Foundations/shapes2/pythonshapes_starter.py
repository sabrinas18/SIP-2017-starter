from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = -250
y_pos = -150
t.setposition(x_pos, y_pos)

### Write your code below:
fillcolor("purple")
n = input('how many sides of a shape?: ')
print(n)
begin_fill()
move = 500
for move in range(n):
    move = forward(180)
    move = right(360/n)
end_fill()







# Close window on click.
exitonclick()

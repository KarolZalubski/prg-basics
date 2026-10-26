import turtle
# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# Side length
side_length = 100

# Draw a square
for i in range(8):
    pen.forward(side_length)
    pen.right(45)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()
import turtle

# create screen
screen = turtle.Screen()
screen.bgcolor("lightblue")   # background color

# create turtle
pen = turtle.Turtle()
pen.pensize(3)
pen.pencolor("purple")

# function to draw square
def draw_square(size):
    for i in range(4):
        pen.forward(size)
        pen.right(90)

# call function
draw_square(150)

turtle.done()

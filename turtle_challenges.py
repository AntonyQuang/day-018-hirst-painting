from turtle import Screen, Turtle
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")
screen = Screen()
screen.colormode(255)
# Challenge 1

def random_colour():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    colour = (r, g, b)
    return colour

def challenge_1():
    """ Draw a square """
    for _ in range (4):
        tim.forward(100)
        tim.right(90)

# challenge_1()

def challenge_2():
    """ Draw a dashed line. Line of 10 paces, gap of 10 paces, 15 times"""
    for _ in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


# challenge_2()

def challenge_3():
    """Draw shapes from triangle to decagon in random shapes """

    for _ in range(3,11):

        tim.pencolor(random_colour())

        for x in range(_):
            angle = 360/_
            tim.forward(100)
            tim.right(angle)


# challenge_3()

def challenge_4():
    """A random walk with different colours at different walk changes"""
    tim.speed(0)
    screen.colormode(255)
    tim.pensize(15)
    for _ in range(200):

        tim.pencolor(random_colour())

        directions = [0, 90, 180, 270]
        direction = random.choice(directions)

        tim.forward(30)
        tim.setheading(direction)


# challenge_4()

def challenge_5(angle_of_gap):
   """Draw a spirograph"""
   tim.speed(0)

   for _ in range(int(360/angle_of_gap)):
       tim.pencolor(random_colour())
       tim.setheading(tim.heading() + angle_of_gap)
       tim.circle(100)



challenge_5(5)





screen.exitonclick()
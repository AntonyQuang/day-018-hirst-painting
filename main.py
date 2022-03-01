from turtle import Turtle, Screen
import turtle
import random
# import colorgram

#
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 10)
#
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     new_color = (red, green, blue)
#     rgb_colors.append(new_color)

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
              (138, 31, 20)]

turtle.shape("arrow")

screen = Screen()
screen.colormode(255)
t = Turtle()
screen.setworldcoordinates(-25, -25, 475, 475)


def paint_a_row():
    t.hideturtle()
    t.penup()
    for _ in range(10):
        color = random.choice(color_list)
        t.dot(20, color)
        t.forward(50)
    t.setheading(90)
    t.forward(50)
    t.setheading(0)
    t.backward(500)


for _ in range(10):
    paint_a_row()

screen.exitonclick()

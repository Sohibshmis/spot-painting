# import colorgram as cg
from colors import colors
import turtle as t
import random as rand

din = t.Turtle()
t.colormode(255)
din.hideturtle()

def random_color():
    return rand.choice(colors)


din.speed("fastest")
din.setheading(225)
din.penup()
din.forward(300)
din.setheading(0)


def reset_din():
    din.left(90)
    din.forward(50)
    din.left(90)
    din.forward(500)
    din.setheading(0)


for x in range(10):
    for _ in range(10):
        din.dot(20, random_color())
        din.forward(50)
    reset_din()

t.Screen().exitonclick()

# Extracting colors from an image

# colors = cg.extract("colors.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)

import colorgram
import random
from turtle import Turtle, Screen
# rgb_colors = []
# colors = colorgram.extract('dot_paint.jpg', 30)
#
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
test
# print(rgb_colors)
screen = Screen()
screen.colormode(255)
color_list = [(233, 233, 232), (231, 233, 237), (236, 231, 233), (224, 233, 227), (207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169)]

# ran_color = random.choice(color_list)
# print(ran_color)
t = Turtle()
t.speed("fastest")
x = 0
y = 50

# t.setheading(225)
# t.penup()
# t.forward(300)
# t.setheading(0)
for _ in range (10):
    for _ in range(10):
        t.pencolor(random.choice(color_list))
        t.dot(20)
        t.penup()
        t.forward(50)

    t.goto(x, y)
    y += 50


screen.exitonclick()
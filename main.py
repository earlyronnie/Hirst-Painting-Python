from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

color_list = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99),
              (122, 175, 156), (229, 236, 239), (226, 198, 131), (242, 247, 244), (192, 87, 108), (11, 50, 64),
              (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77)]

boop = Turtle()
boop.hideturtle()
cs = 10
space = 50
area = 10

boop.speed("fastest")
boop.penup()
boop.goto(-200, -270)
boop.pendown()


def go_back():
    boop.penup()
    boop.left(90)
    boop.forward(50)
    boop.left(90)
    boop.setx(-200)
    boop.left(90)
    boop.left(90)
    boop.pendown()


def first_line(num):
    for _ in range(num):
        random_color = random.choice(color_list)
        boop.begin_fill()
        boop.fillcolor(random_color)
        boop.color(random_color)
        boop.circle(cs)
        boop.end_fill()
        boop.penup()
        if _ < (num - 1):
            boop.forward(space)
        else:
            boop.pendown()


def next_line(num):
    for _ in range(num):
        go_back()
        first_line(10)


first_line(area)
next_line(area)
screen.exitonclick()

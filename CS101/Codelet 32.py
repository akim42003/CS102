from turtle import *
from random import randint, choice

BUTTON_RADIUS = 40

class Button:
    def __init__(self, loc, color):
        self.location = loc
        self.fillcolor = color
    def display(self, t):
        t.penup()
        t.goto(self.location)
        t.pendown()
        t.width(3)
        t.pencolor("white")
        t.fillcolor(self.fillcolor)
        t.begin_fill()
        t.circle(BUTTON_RADIUS)
        t.end_fill()
    

def main():
    t = Turtle()
    tracer(0)
    window = Screen()
    window.bgcolor("black")
    buttons = []
    for b in range(30):
        loc = (randint(-200, 200), randint(-200, 200))
        color = choice(["red", "green", "blue", "gray"])
        buttons.append(Button(loc, color))
    for button in buttons:
        button.display(t)
    update()

main()
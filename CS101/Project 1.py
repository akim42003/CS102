#Libraries
from turtle import *
import random
from math import *

#Screen 
screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")
colormode(255)

#Turtle 
planet = Turtle()
planet.shape("turtle")
planet.pensize(1)
planet.pencolor("white")
planet.speed(10)

sun = Turtle()
sun.shape = ("turtle")
sun.pensize(1)
sun.pencolor("white")
sun.speed(10)

def draw_sun(planet_num):
    sun.begin_fill()
    sun.fillcolor("yellow")
    sun_x = random.randint(-150, 150)
    sun.penup()
    sun.goto(sun_x, 120)
    sun.pendown()
    sun.circle(400/planet_num**2)
    sun.end_fill()
    sun.hideturtle()
def draw_stars():
    for stars in range(40):
        star_x = random.randint(-400, 400)
        star_y = random.randint(-400, 400)
        sun.penup()
        sun.goto(star_x, star_y)
        sun.pendown()
        sun.dot(10)


def space_planet(planet_type):
    valid_planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    for world in valid_planets:
        if valid_planets.index(planet_type) >= 0:
                planet_num = 1
                planet.penup()
                planet.goto(random.randint(-200,200),random.randint(0,200))
                planet.pendown()
                planet.begin_fill()
                planet.circle(16)
                planet.fillcolor("gray")
                planet.end_fill()
                planet.hideturtle()
        if valid_planets.index(planet_type) >= 1:
                planet_num = 2
                planet.penup()
                planet.goto(random.randint(-200,200),random.randint(-200,0))
                planet.pendown()
                planet.begin_fill()
                planet.circle(38/planet_num)
                planet.fillcolor("orange")
                planet.end_fill()
                planet.hideturtle()
        if valid_planets.index(planet_type) >= 2:
                planet_num = 3
                planet.penup()
                planet.goto(random.randint(-200,200),random.randint(-200,0))
                planet.pendown()
                planet.begin_fill()
                planet.circle(60/planet_num)
                planet.fillcolor("green")
                planet.end_fill()
                planet.hideturtle()
        if valid_planets.index(planet_type) >= 3:
                planet_num = 4
                planet.penup()
                planet.goto(random.randint(-200,200),random.randint(-200,0))
                planet.pendown()
                planet.begin_fill()
                planet.circle(50/planet_num)
                planet.fillcolor("red")
                planet.end_fill()
                planet.hideturtle()
        if valid_planets.index(planet_type) >= 4:
                planet_num = 5
                planet.penup()
                planet.goto(random.randint(-200,200), random.randint(-150,0))
                planet.pendown()
                planet.begin_fill()
                planet.circle(240/planet_num)
                planet.fillcolor("dark orange")
                planet.end_fill()
                planet.penup()
                planet.left(100)
                planet.forward(125/planet_num)
                planet.pendown()
                planet.begin_fill()
                planet.fillcolor("firebrick")
                planet.circle(80/planet_num)
                planet.end_fill()
                planet.hideturtle()
        if valid_planets.index(planet_type) >= 5:
                planet_num = 6
                planet.penup()
                planet.goto(random.randint(-100,100),random.randint(-100,0))
                planet.pendown()
                planet.begin_fill()
                planet.circle(220/planet_num)
                planet.fillcolor("peru")
                planet.end_fill()
                planet.penup()
                planet.backward(200/planet_num)
                planet.pendown()
                for half in range(2):
                    planet.circle(360/planet_num,90)
                    planet.circle(360/planet_num/3,90)
                planet.hideturtle()
        if valid_planets.index(planet_type) >= 6:
                planet_num = 7
                planet.penup()
                planet.goto(random.randint(-100,100),random.randint(-100,0))
                planet.pendown()
                planet.begin_fill()
                planet.circle(200/planet_num)
                planet.fillcolor("powder blue")
                planet.end_fill()
                planet.hideturtle()
        if valid_planets.index(planet_type) >= 7:
                planet_num = 8
                planet.penup()
                planet.goto(random.randint(-100,100),random.randint(-100,0))
                planet.pendown()
                planet.begin_fill()
                planet.circle(180/planet_num)
                planet.fillcolor("blue")
                planet.end_fill()
                planet.hideturtle()
        return planet_num
def main():
    planet_type=input("What planet do you want first?")
    draw_stars()
    planet_num = space_planet(planet_type)
    draw_sun(planet_num)

main()
exitonclick()

from turtle import *
from random import randint

LIGHT_SIZE = 60

class Light:
    
    def __init__(self, loc):
        self.location = loc
        
    def display(self, bulb, on_off):
        bulb.up()
        bulb.goto(self.location)
        bulb.down()
        bulb.width(5)
        if on_off == 1:
            bulb.fillcolor("darkgreen")
        if on_off == 2:
            bulb.fillcolor("lightgreen")
        bulb.begin_fill()
        for side in range(4):
            bulb.forward(LIGHT_SIZE)
            bulb.left(90)
        bulb.end_fill()
        
def main():
    # Create a turtle object named bulb:
    bulb = Turtle()
    on_off=0
    # Set up the graphics window:
    window = Screen()
    window.bgcolor("blanchedalmond")
    
    offset = int(5 * LIGHT_SIZE / 2)
    for x in range(-offset, offset, LIGHT_SIZE):
        on_off = randint(1,2)
        l = Light((x, 0))
        l.display(bulb, on_off)
    
main()
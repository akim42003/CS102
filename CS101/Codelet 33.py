from turtle import *
from functools import partial
import random

LIGHT_SIZE = 75

class Light:
    def __init__(self, loc, id_num, neighbors):
        self.location = loc
        self.on = random.choice([True, False])
        self.id = id_num
        self.neighbors = neighbors
    def display(self, bulb):
        bulb.up()
        bulb.goto(self.location)
        bulb.down()
        bulb.width(5)
        bulb.fillcolor("lightgreen" if self.on else "darkgreen")
        bulb.begin_fill()
        for side in range(4):
            bulb.forward(LIGHT_SIZE)
            bulb.left(90)
        bulb.end_fill()

def display_lights(lights, bulb):
    on_off = 0
    for light in lights:
        light.display(bulb)
        if light.on == False:
            on_off += 1
    if on_off == 25:
        print("Game Over")
        return
    update()

def mouse_clicked(lights, bulb, x, y):
    # Check which light just got clicked:
    for light in lights:
        light_x = light.location[0]
        light_y = light.location[1]
        if x > light_x and x < light_x + LIGHT_SIZE and y > light_y and y < light_y + LIGHT_SIZE:
            light.on = not light.on
            # Check the neighbors of the clicked light, and toggle them too!
            for neighbor in light.neighbors:
                    lights[neighbor].on = not lights[neighbor].on
    
    display_lights(lights, bulb)

def main():
    bulb = Turtle()
    tracer(0)
    window = Screen()
    window.bgcolor("blanchedalmond")
    
    # Create and display the lights:
    offset = int(LIGHT_SIZE * 5 / 2)
    lights = []
    id_num = 0
    for x in range(-offset, -offset + LIGHT_SIZE * 5, LIGHT_SIZE):
        for y in range(-offset, -offset + LIGHT_SIZE * 5, LIGHT_SIZE):
            neighbors = []
            if id_num - 1 >= 0 and id_num % 5 != 0:
                neighbors.append(id_num - 1)
            if id_num + 1 <= 24 and (id_num + 1) % 5 != 0:
                neighbors.append(id_num + 1)
            if id_num - 5 >= 0:
                neighbors.append(id_num - 5)
            if id_num + 5 <= 24:
                neighbors.append(id_num + 5)        
            lights.append(Light((x, y), id_num, neighbors))
            id_num = id_num + 1
    
    
    display_lights(lights, bulb)
    
    
    window.onclick(partial(mouse_clicked, lights, bulb))
    window.mainloop()


main()
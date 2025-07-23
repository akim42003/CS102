from PIL import Image
import random

def get_average_color(x_coord, y_coord, size, image):
    
    cell_check = random.randint(0, size*size-1)
    counter = 0
    for x in range(x_coord, x_coord + size):
        for y in range(y_coord, y_coord + size):
            if cell_check == counter:
                (r, g, b) = image.getpixel((x,y))
                return r, g, b
            counter += 1

        
            

def shrink(image, blank, size):
    for x in range(0, image.width, size):
        for y in range(0, image.height, size):
            (r, g, b) = get_average_color(x, y, size, image)
            blank.putpixel((int(x / size), int(y / size)), (r, g, b))
            
def main():
    size = int(input("Enter a number of pixels: "))
    
    cat = Image.open("cat.jpeg")
    cat.show()
    new = Image.new(mode="RGB", size=(int(cat.width/size), int(cat.height/size)), color = (255, 255, 255))

    shrink(cat, blank, size)
    new.show()

main()
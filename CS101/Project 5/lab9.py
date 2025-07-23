"""
Lab: Image manipulation
"""

from PIL import Image

def main():
    my_image = Image.open("alex.jpg")
    posterize(my_image)
    #my_image.show()
#     rgbav=int(input("enter a rgbav:"))
#     blackwhite(my_image,rgbav)
    my_image.show()
    # Remove this pass, and write your code here

def posterize(my_image):
    for xi in range(my_image.width):
        for yi in range(my_image.height):
            RGB = list(my_image.getpixel((xi,yi)))
            Blue = 0
            Buff = 0
            white = 0
            value = 0
            for index in range(3):
                value += RGB[index]
            if value<=255:
                RGB[0] = 0
                RGB[1] = 47
                RGB[2] = 134
            elif value in range(256,510):
                RGB[0] = 214
                RGB[1] = 186
                RGB[2] = 139
            elif value in range(511,765):
                RGB[0] = 255
                RGB[1] = 255
                RGB[2] = 255
            my_image.putpixel((xi,yi),(RGB[0],RGB[1],RGB[2]))
    return my_image




def red_filter(image):
    """Takes an image, and makes it more red.
    This is a template for many useful functions!"""
    
    for x in range(image.width):
        print("Working on column", x) ### To see how long it will take
        
        for y in range(image.height):
            
            ## This tuple assignment gets the r, g, and b components
            ## of the pixel's color
            (r,g,b) = image.getpixel((x, y))
            image.putpixel((x,y,),(r+100,g,b))
            ### Put code here to correctly change the pixel's color


def blackwhite(image,rgbav):
    for x in range(image.width):
        print("Working on column", x) ### To see how long it will take
        
        for y in range(image.height):
            
            ## This tuple assignment gets the r, g, and b components
            ## of the pixel's color
            (r,g,b) = image.getpixel((x, y))
            if r>rgbav:
                image.putpixel((x,y,),(255,0,0))
            elif b>rgbav and g>rgbav:
                image.putpixel((x,y,),(0,255,255))
            elif b>rgbav:
                image.putpixel((x,y,),(0,255,0))
            elif g>rgbav:
                image.putpixel((x,y,),(0,255,0))
            else:
                image.putpixel((x,y,),(255,255,255))


    

if __name__ == "__main__":
    main()

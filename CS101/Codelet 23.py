from PIL import Image

image = Image.open("chapel.jpg")

def get_data(image):
    total_grey = []
    coordinates = []
    for x in range(0, image.width):
        for y in range(0, image.height):
            coord = (x,y)
            coordinates.append(coord)
            (r,g,b) = image.getpixel((x,y))
            grey = ((r+g+b)//3)
            total_grey.append(grey)
    
    brightest = max(total_grey)
    index = total_grey.index(brightest)
    brightest_coord = coordinates[index]
    print("The pixel at", brightest_coord, "has brightness", brightest)
def main():
    get_data(image)
    

main()
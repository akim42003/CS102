from PIL import Image

def count_pixels(nasi, brightness):
    result = 0
    for x in range(0, nasi.width):
        for y in range(0, nasi.height):
            (r, g, b) = nasi.getpixel((x,y))
            bright = ((r + g + b)//3)
            if bright >= brightness:
                result += 1
    return result
            


def main():
    nasi = Image.open("nasi_minyak.jpg")
    nasi.show()
    
    brightness = int(input("Enter a brightness: "))
    
    result = count_pixels(nasi, brightness)
    print(f"There are {result} pixels that are at least of brightness {brightness}.")

main()
# Partnered with Will Swartz 
from PIL import Image
from math import sqrt
import random
from matplotlib import colors
def main():
    my_image = Image.open("alex.jpg")
    sections=int(input("enter a square number"))
    shaded_squares = shadedsquares(sections)
    colors=["red","black","green","cyan","blue","yellow","midnightblue"]
    splitsections(sections,my_image,colors,shaded_squares)
    my_image.show()
    pass


def shadedsquares(sections):
    sq=[]
    answer=""
    while answer != "end":
        answer=input("enter squares you want to shade(1-"+ str(sections) +")")
        if answer=="all":
            sq=[]
            for i in range(sections):
                sq.append(str(i+1))
        elif answer !="end":
            sq.append(answer)
    return sq

def splitsections(sections,my_image,colors,shaded_squares):
    sectionside=int(sqrt(sections))
#     print(sectionside)
    counter = 0
    for i in range (sectionside):
        for j in range(sectionside):
            counter += 1
            if str(counter) in shaded_squares:
                posterize(my_image,i*(my_image.width/sectionside),j*(my_image.height/sectionside),sectionside,colors)

def posterize(image,xi,yi,sectionside,color):
    newcolors=[]
    randomsamples=random.sample(range(len(color)), 3)
    for i in range(3):
        newcolors.append(color[randomsamples[i]])
    RGBnew=[]
    for i in newcolors:
        RGBnew+=[colors.to_rgb(i)]
    for x in range(int(xi),int(xi+image.width/sectionside)):
        
        for y in range(int(yi),int(yi+image.height/sectionside)):
            RGB = list(image.getpixel((x,y)))
            value=0
            for index in range(3):
                value += RGB[index]
            if value<=255:
                RGB[0] = int(RGBnew[0][0]*255)
                RGB[1] = int(RGBnew[0][1]*255)
                RGB[2] = int(RGBnew[0][2]*255)
            elif value in range(256,510):
                RGB[0] = int(RGBnew[1][0]*255)
                RGB[1] = int(RGBnew[1][1]*255)
                RGB[2] = int(RGBnew[1][2]*255)
            elif value in range(511,765):
                RGB[0] = int(RGBnew[2][0]*255)
                RGB[1] = int(RGBnew[2][1]*255)
                RGB[2] = int(RGBnew[2][2]*255)
            image.putpixel((x,y),(RGB[0],RGB[1],RGB[2]))
    
if __name__ == "__main__":
    main()
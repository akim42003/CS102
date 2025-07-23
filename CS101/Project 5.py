

from PIL import Image, ImageDraw
import cv2
colors = ["red", "blue", "green", "black", "purple", "pink", "white", "yellow", "orange", "teal"]
canvas = Image.new("RGB", (500, 500), (255,255,255))
canvas.save("blank.jpg")

img = cv2.imread("blank.jpg")
image = Image.fromarray(img)
draw = ImageDraw.Draw(image, "RGBA")
on_off_event = None
# show image
cv2.imshow("blank.jpg", img)
# draw = ImageDraw
# .Draw(image, "RGBA")

def mouse_click(event, x, y, flags, param):
    global img, on_off_event
    # check if left click
    if event == cv2.EVENT_LBUTTONDOWN:
        on_off_event = True
    if event == cv2.EVENT_MOUSEMOVE:
        if on_off_event == True:
            cv2.circle(img, (x,y), 2, (255,0,255), -1)
            cv2.imshow('image', img)
    if event == cv2.EVENT_LBUTTONUP:
        print("off")
        on_off_event = False
        return on_off_event

def continue_drawing():
    global on_off_event
    cont = input("Continue Drawing?")
    if cont == "yes":
        on_off_event = True
    if cont == "no":
        on_off_event = False

def main():
    x=0
    y=0
    event = False
    flags = None
    param = None
    mouse_click(event, x, y, flags, param)
    cv2.setMouseCallback("blank.jpg", mouse_click)
    while True:
        cv2.imshow("blank.jpg", img)
        if on_off_event == False:
            print("restart")
            main()

    # print(on_off_event)
    # image.show()
    # close all the opened windows.
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()

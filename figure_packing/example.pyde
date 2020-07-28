from collections import deque
import random
from math import sqrt
import datetime

image_file = "monalisa.jpg"
img = None
iterations = 2000
current_gen = 0
shapes = deque()
begin_time = datetime.datetime.now()


def setup():
    global img
    size(100, 100)
    frameRate(10000)
    img = loadImage(image_file)
    this.surface.setResizable(True)
    this.surface.setSize(img.width, img.height)
    background(255)

    img.loadPixels()

def average_color(shape_x, shape_y, width, height):
    #img.loadPixels() should be called by now in setup(). Better to call it once there instead of many times here
    r, g, b = 0, 0, 0
    pixels = 0
    for y in range(shape_y, shape_y + height):
        for x in range(shape_x, shape_x + width):
            img_color = img.get(x, y)
            r += red(img_color) ** 2
            g += green(img_color) ** 2
            b += blue(img_color) ** 2

            pixels += 1

    return [sqrt(r/pixels), sqrt(g/pixels), sqrt(b/pixels)]


def draw():  
    global current_gen
    if current_gen > iterations:
        noLoop()
        print(datetime.datetime.now() - begin_time)
    

    shape_width = random.randint(int(img.width * 0.01), int(img.width * 0.10))
    shape_height = random.randint(int(img.height * 0.01), int(img.height * 0.10))
    shape_x = random.randint(0, img.width - shape_width)
    shape_y = random.randint(0, img.height - shape_height)

    filler_shape = createShape(RECT, shape_x, shape_y, shape_width, shape_height)
    avg_color = average_color(shape_x, shape_y, shape_width, shape_height)
    filler_shape.setFill(color(avg_color[0], avg_color[1], avg_color[2], 80))
    filler_shape.setStroke(color(avg_color[0], avg_color[1], avg_color[2], 80))
    shape(filler_shape)    

    current_gen += 1

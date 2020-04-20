import random

max_depth = 0
angle = PI / 4
color_purple = [161, 3, 252, 100]
color_pink = [252, 3, 107, 100]
length_multiplier = 0.67

def setup():
    size(800, 600)
    noLoop()
    

def draw():
    background(51)
    strokeWeight(2)
    stroke(255)
    translate(width/2, height)
    tree(200)

def tree(l, depth=0):
    if depth == max_depth:
        if depth != 0:
            c = random.choice([color_pink, color_purple])
            stroke(*c)
            fill(*c)
            ellipse(0, 0, 15, 15)
        return
    
    stroke(255)
    line(0, 0, 0, -l)
    translate(0, -l)
    pushMatrix()
    rotate(angle)
    tree(l*length_multiplier, depth+1)
    popMatrix()
    pushMatrix()
    rotate(-angle)
    tree(l*length_multiplier, depth+1)
    popMatrix()


def keyPressed():
    global angle, max_depth
    if keyCode == LEFT:
        angle -= PI / 24
    elif keyCode == RIGHT:
        angle += PI / 24
    elif keyCode == UP:
        max_depth += 1
    elif keyCode == DOWN:
        max_depth -= 1
        max_depth = max(0, max_depth)
    elif key == ENTER:
        save("tree.jpg")
    redraw()

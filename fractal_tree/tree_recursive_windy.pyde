import random

max_depth = 0
max_rotation = 0
color_pink = [252, 3, 107, 100]
leaf_color = color_pink
length_multiplier = 0.67
wind = 0

tx = 0
ty = 1000


def setup():
    size(800, 600)
    
def draw():
    global tx, ty, wind
    tx += 0.01
    ty += 0.01
    background(60)
    strokeWeight(2)
    stroke(255)
    translate(width/2, height)
    update_wind()
    tree(200, 6)

def tree(l, stroke_weight, depth=0):
    if depth == max_depth:
        if depth != 0:
            draw_leaf(0, 0)
        return
    
    stroke(255)
    strokeWeight(stroke_weight)

    line(0, 0, 0, -l)
    translate(0, -l)
    
    pushMatrix()
    right_rotation = 0.25 + noise(tx) * 0.25 - wind * 20
    right_rotation = min(PI/2, right_rotation)
    right_rotation = max(0, right_rotation)
    rotate(right_rotation)
    tree(l*length_multiplier, stroke_weight * 0.8, depth+1)
    popMatrix()
    
    pushMatrix()
    left_rotation = -0.25 -noise(ty) * 0.25 - wind * 20
    left_rotation = max(-PI/2, left_rotation)
    left_rotation = min(0, left_rotation)
    rotate(left_rotation)
    tree(l*length_multiplier, stroke_weight * 0.8, depth+1)
    popMatrix()

def draw_leaf(x, y):
    stroke(*leaf_color)
    fill(*leaf_color)
    ellipse(x, y, 15, 15)

def update_wind():
    global wind
    if not mousePressed:
        wind -= wind * 0.05 #slowly transition towards 0 to avoid sudden jumps
        return

    mouse_dist = dist(width/2, 0, mouseX, 0)
    if mouse_dist == 0: #avoid division by zero
        mouse_dist = 1
    
    max_wind = 1 / mouse_dist
    max_wind = min(0.015, max_wind)
    if mouseX < width / 2: #to the left of the tree causes negative winds
        wind -= max_wind * 0.05 #slowly transition wind to max_wind to avoid sudden jumps
        wind = max(wind, -max_wind) 
    else:
        wind += max_wind * 0.05
        wind = min(wind, max_wind) #slowly transition wind to max_wind to avoid sudden jumps


def keyPressed():
    global max_depth
    if keyCode == UP:
        max_depth += 1
    elif keyCode == DOWN:
        max_depth -= 1
        max_depth = max(0, max_depth)
    elif key == ENTER:
        save("tree.jpg")
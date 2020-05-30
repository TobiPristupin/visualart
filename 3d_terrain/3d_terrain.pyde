scale = 10
cols, rows = None, None
w = 1400
h = 850
elevation = None
flying_offset = 0
color_pink = [252, 3, 107, 50]


def setup():
    global cols, rows
    size(800, 600, P3D)
    # frameRate(5)
    cols = w / scale
    rows = h / scale
    # noLoop()

def draw():
    global flying_offset
    background(0)
    noFill()
    stroke(255)
    translate(width/2, height/2)
    rotateX(PI / 3)
    translate(-w/2, -h/2)

    elevation = calculate_elevation()
    stroke(*color_pink)
    fill(*color_pink)
    for y in range(rows-1):
        beginShape(TRIANGLE_STRIP)
        for x in range(cols):
            vertex(x*scale, y*scale, elevation[x][y])
            vertex(x*scale, (y+1)*scale, elevation[x][y+1])
        endShape()
    
    flying_offset -= 0.05
    
def calculate_elevation():
    elevation = [[0 for i in range(rows)] for j in range(cols)]

    ty = flying_offset
    for y in range(rows):
        tx = 0
        for x in range(cols):
            elevation[x][y] = map(noise(tx, ty), 0, 1, -125, 125)
            tx += 0.05
        ty += 0.05
    return elevation
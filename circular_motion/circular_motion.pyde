# class Ball :

#     def __init__(self, x, y, m):
#         self.pos = PVector(x, y)
#         self.vel = PVector(0, 1)
#         self.acc = PVector(0, 0)
    
#     def update(self):
#         self.vel += self.acc
#         self.pos += self.vel

#     def add_forces(self, *forces):
#         self.acc.mult(0)
#         for force in forces:
#             self.acc += force

#     def display(self):
#         stroke(255)
#         fill(255)
#         ellipse(self.pos.x, self.pos.y, 30, 30)

# ball = None
# radius = PVector(50, 0)

# def setup():
#     global ball
#     size(800, 600)
#     ball = Ball(radius.x, radius.y, 10)
#     frameRate(1)

# def draw():
#     background(51)
#     translate(width/2, height/2)

#     centripetal_force = PVector.sub(radius, ball.pos)
#     line(radius.x, radius.y, centripetal_force.x, centripetal_force.y)
#     print(centripetal_force)
#     radius_length = radius.mag()
#     centripetal_force.setMag(ball.vel.magSq() / radius.mag()) #v^2/r
#     ball.add_forces(centripetal_force)
#     ball.update()

#     ball.display()

# def setup():
#     size(800, 600)
#     noLoop()

# def draw():
#     background(51)
#     translate(width/2, height/2)
#     noFill()
#     stroke(255)
#     strokeWeight(5)
    
#     arcs = 4
#     for i in range(arcs):
#         start = TWO_PI / arcs * i
#         end = TWO_PI / arcs * (i + 1)
#         stroke(random(0, 255), random(0, 255), random(0, 255))
#         arc(0, 0, 200, 200, start, end)
#         arc(0, 0, 150, 100, start, end)
#         arc(0, 0, 100, 100, start, end)
# def setup():
#     size(800, 600)
#     noLoop()

# def draw():
#     background(51)
#     translate(width/2, height/2)
#     noFill()
#     stroke(255)
#     strokeWeight(5)
    
#     arcs = 4
#     for i in range(arcs):
#         start = TWO_PI / arcs * i
#         end = TWO_PI / arcs * (i + 1)
#         stroke(random(0, 255), random(0, 255), random(0, 255))
#         arc(0, 0, 200, 200, start, end)
#         arc(0, 0, 150, 100, start, end)
#         arc(0, 0, 100, 100, start, end)



def setup():
    size(800, 600)
    noLoop()

def draw():
    background(51)
    translate(width/2, height/2)
    noFill()
    stroke(255)
    strokeWeight(5)
    
    arcs = 4
    for i in range(arcs):
        start = TWO_PI / arcs * i
        end = TWO_PI / arcs * (i + 1)
        stroke(random(0, 255), random(0, 255), random(0, 255))
       
def setup():
    size(800, 600)
    noLoop()

def draw():
    background(51)
    translate(width/2, height/2)
    noFill()
    stroke(255)
    strokeWeight(5)
    
    arcs = 60
    for i in range(arcs):
        start = TWO_PI / arcs * i
        end = TWO_PI / arcs * (i + 1)
        stroke(random(0, 255), random(0, 255), random(0, 255))
        arc(random(0, 10), random(0, 10), 300, 300, start, end)

import random

balls = []

def setup():
    global balls
    size(600, 200)
    num_balls = 20
    diameter = width/num_balls
    for i in range(num_balls):
        balls.append(Ball(diameter, i*diameter+diameter/2, random.random()*5))
    
def draw():
    global balls
    fill(0, 12)
    rect(0, 0, width, height)
    for b in balls:
        b.display()
        b.move()
        

    
    
class Ball:
    
    def __init__(self, diameter, x, velocity):
        self.diameter = diameter
        self.radius = diameter/2
        self.x = x
        self.y = self.radius
        self.velocity = velocity
        self.dir = 1
        
    def move(self):
        if self.y + self.radius > height or self.y - self.radius < 0:
            self.dir *= -1
        self.y += self.velocity * self.dir
    
    def display(self):
        c = map(self.velocity, 0, 5, 80, 255)
        stroke(c, 0, 0)
        fill(c, 0, 0)
        ellipse(self.x, self.y, self.diameter, self.diameter)

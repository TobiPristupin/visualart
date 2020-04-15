class Ball:
    
    def __init__(self, mass):
        self.pos = PVector(0, 0)
        self.velocity = PVector(0, 0)
        self.velocity.limit(1)
        self.acceleration = PVector(0, 0)
        self.mass = mass
        self.radius = self.mass * 8
        self.collision_energy = 1
        
    def update(self):
        self.velocity.add(self.acceleration)
        self.pos.add(self.velocity)
        self.acceleration.mult(0)
        self.check_edges()
        
    def add_forces(self, *forces):
        for force in forces:
            f = force.get()
            f.div(self.mass)
            self.acceleration.add(f)
        
    def check_edges(self):
        if self.pos.x + self.radius > width:
            self.pos.x = width - self.radius
            self.velocity.x *= -1 * self.collision_energy
        elif self.pos.x - self.radius < 0:
            self.pos.x = self.radius
            self.velocity.x *= -1 * self.collision_energy
            
        if self.pos.y + self.radius > height:
            self.pos.y = height - self.radius
            self.velocity.y *= -1 * self.collision_energy
        if self.pos.y - self.radius < 0:
            self.pos.y = self.radius
            self.velocity.y *= -1 * self.collision_energy
        
    def display(self):
        fill(0, 0, 0, 128)
        stroke(0)
        strokeWeight(2)
        ellipse(self.pos.x, self.pos.y, self.radius*2, self.radius*2)
        

balls = []
num_balls = 20

def setup():
    global balls
    size(600, 400)
    balls = [Ball(random(0.1, 5)) for i in range(num_balls)]

def draw():
    global ball
    background(255)
    
    wind = PVector(0.01, 0)

    for b in balls:
        gravity_center = PVector(b.pos.x, height*100)
        gravity = PVector.sub(gravity_center, b.pos)
        gravity.setMag(1/(gravity_center.dist(b.pos)))
        gravity.mult(4000 * b.mass)
        
        b.add_forces(gravity, wind)
        b.update()
        b.display()

import random

branches = []
num_branches = 100


class Branch:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.prev_x = x
        self.prev_y = y
        self.x_velocity = 0
        self.y_velocity = 0
        self.visible = True
        self.tx = random.randint(1, num_branches * 100)
        self.ty = random.randint(num_branches * 100 + 100, num_branches * 100 + 100 + num_branches * 100)

    def move(self):
        stroke((millis() * 0.3) % 360, 100, 50)
        strokeWeight(2)
        self.x_velocity = map(noise(self.tx), 0, 1, -20, 20)
        self.y_velocity = map(noise(self.ty), 0, 1, -20, 20)
        self.prev_x, self.prev_y = self.x, self.y
        self.x, self.y = self.x + self.x_velocity, self.y + self.y_velocity
        line(self.prev_x, self.prev_y, self.x, self.y)
        self.tx += 0.02
        self.ty += 0.02

        self.updateVisibility()

    def updateVisibility(self):
        if self.x > width or self.x < 0 or self.y > height or self.y < 0:
            self.visible = False


def setup():
    global branches, num_branches
    size(600, 600)
    background(0)
    colorMode(HSB)
    blendMode(SCREEN)
    for i in range(num_branches):
        branches.append(Branch(width/2, height/2))


def draw():
    for branch in branches:
        if branch.visible:
            branch.move()

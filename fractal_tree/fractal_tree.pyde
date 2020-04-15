import random

depth = 1
max_depth = 10
angle = PI / 4
length_multiplier = 0.67
mass_multiplier = length_multiplier
root_mass = 10
branches = []
leaves = []

class Branch :
    
    def __init__(self, begin, end, mass):
        self.begin = begin
        self.end = end
        self.mass = mass
        self.has_children = False

    def display(self):
        stroke(255)
        line(self.begin.x, self.begin.y, self.end.x, self.end.y)

    def left_branch(self, angle, length_multiplier, mass_multiplier):
        return self.__branch(-angle, length_multiplier, mass_multiplier)

    def right_branch(self, angle, length_multiplier, mass_multiplier):
        return self.__branch(angle, length_multiplier, mass_multiplier)

    def __branch(self, angle, length_multiplier, mass_multiplier):
        dir = PVector.sub(self.end, self.begin)
        dir.rotate(angle)
        dir.mult(length_multiplier)
        new_end = PVector.add(dir, self.end)
        branch = Branch(self.end, new_end, self.mass * mass_multiplier)
        return branch

class Leaf :

    purple = [161, 3, 252, 100]
    pink = [252, 3, 107, 100]

    def __init__(self, x, y, w, mass):
        self.x = x
        self.y = y
        self.w = w
        self.mass = mass
        self.color = random.choice([Leaf.purple, Leaf.pink])

    def display(self):
        stroke(*self.color)
        fill(*self.color)
        ellipse(self.x, self.y, self.w, self.w)

def build_tree():
    global branches
    
    del branches[:]
    del leaves[:]
    
    start = PVector(width/2, height)
    end = PVector(width/2, height - 150)
    root = Branch(start, end, root_mass)
    branches.append(root)

    for i in range(max_depth - 1):
        length = len(branches)
        for j in range(length):
            if not branches[j].has_children:
                left = branches[j].left_branch(angle, length_multiplier, mass_multiplier)
                right = branches[j].right_branch(angle, length_multiplier, mass_multiplier)
                branches.append(left)
                branches.append(right)
                branches[j].has_children = True

    build_leaves()

def build_leaves():
    global leaves
    del leaves[:]
    for branch in branches:
        leaves.append(Leaf(branch.end.x, branch.end.y, 20, 1))

def setup():
    global branches
    size(800, 600)
    build_tree()
    build_leaves()

def draw():
    background(51)
    strokeWeight(3)

    for i in range(2**depth - 1):
        branches[i].display()
    
    start = 2**(depth-1) - 1
    end = 2**(depth) - 1
    for i in range(start, end): #only display leaves that correspond to final level
        leaves[i].display()
     
def keyPressed():
    global angle, depth
    if keyCode == LEFT:
        angle -= PI / 24
        build_tree()
        build_leaves()
    elif keyCode == RIGHT:
        angle += PI / 24
        build_tree()
        build_leaves()
    elif keyCode == UP:
        depth += 1
        depth = min(max_depth, depth)
    elif keyCode == DOWN:
        depth -= 1
        depth = max(0, depth)
    elif key == ENTER:
        save("tree.jpg")
    redraw()

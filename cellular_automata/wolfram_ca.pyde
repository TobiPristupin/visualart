import random
from collections import deque

width, height = 600, 600

cell_width = 10
cell_height = 10
num_cells = width / cell_width
generations = deque()
rule = 30
ruleset = list(map(int, format(rule, "08b")))

def setup():
    size(width, height)
    frameRate(8)

def draw():
    background(255)
    stroke(0)
    for y, generation in enumerate(generations):
        for x, cell in enumerate(generation):
            if cell: fill(255)
            else: fill(0)

            rect(x*cell_width, y*cell_height, cell_width, cell_height)

    update_generations()

    if len(generations) > height / cell_width:
        generations.popleft()     

def update_generations():
    global generations
    if len(generations) == 0:
        generations.append([0 for i in range(num_cells)])
        generations[0][len(generations[0]) // 2] = 1
        return 

    current_gen = generations[-1]    
    new_gen = list(current_gen)

    for i in range(1, len(current_gen) - 1):
        new_gen[i] = apply_rule(current_gen[i-1], current_gen[i], current_gen[i+1])

    generations.append(new_gen)

def apply_rule(left, center, right):
    concat = str(left) + str(center) + str(right)
    index = int(concat, 2)
    return list(reversed(ruleset))[index]





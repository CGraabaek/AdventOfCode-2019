import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

print("Advent Of Code - Day 3")

PUZZLEINPUT = open('input.txt', 'r').read().split('\n')

wire_1 = PUZZLEINPUT[0].strip().split(',')
wire_2 = PUZZLEINPUT[1].strip().split(',')

def manhattan_distance(pos):
    return abs(pos[0]) + abs(pos[1])

def get_posistion(wire):
    #Initial postions
    x, y = 0, 0

    positions = set()

    for i in range(0,len(wire)):
       #Increment the position with one for each of the commands lenght
        for j in range(0,int(wire[i][1:])):
            
            direction = wire[i][0]
            
            if  direction == "R":
                x +=1
            elif direction == "L":
                x -=1
            elif direction == "U":
                y -=1
            elif direction == "D":
                y +=1
            
            positions.add((x, y))
    
    return positions


positions_1 = get_posistion(wire_1)
positions_2 = get_posistion(wire_2)

intersections = positions_1.intersection(positions_2)
manhattan_distances = []

for intersection in intersections:
    manhattan_distances.append(manhattan_distance(intersection))

print(f'Part 1: {min(manhattan_distances)}')
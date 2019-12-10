print("Advent Of Code - Day 10")

PUZZLEINPUT = open('input.txt', 'r').read().split("\n")
x_coor = len(PUZZLEINPUT[0]) 
y_coor = len(PUZZLEINPUT)

asteroid_map = [(x,y) for y in range(0,y_coor) for x in range(0,x_coor) if PUZZLEINPUT[y][x] == "#"]

print(asteroid_map)
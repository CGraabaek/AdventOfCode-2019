import math
from collections import defaultdict


print("Advent Of Code - Day 10")

PUZZLEINPUT = open('input.txt', 'r').read().split("\n")
x_coor = len(PUZZLEINPUT[0]) 
y_coor = len(PUZZLEINPUT)

asteroid_map = [(x,y) for y in range(0,y_coor) for x in range(0,x_coor) if PUZZLEINPUT[y][x] == "#"]

def find_station_locations(p1, p2):
    #inspired by https://python-forum.io/Thread-finding-angle-between-three-points-on-a-2d-graph
    return math.degrees(math.atan2(p1[0] - p2[0], p1[1] - p2[1]))

stations = defaultdict(set)

for asteroid_1 in asteroid_map:
    for asteroid_2 in asteroid_map:
        if asteroid_1 == asteroid_2:
            continue
        stations[asteroid_1].add(find_station_locations(asteroid_1, asteroid_2))

print(f'Part 1: {len(max(stations.values(), key=len))}')
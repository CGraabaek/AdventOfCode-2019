print("Advent Of Code - Day 1")

PUZZLEINPUT = open('input.txt', 'r').read().split("\n")
## Part 1
data = [int(i) for i in PUZZLEINPUT]
part_1_sum = 0
part_2_sum = 0

for line in data:
    part_1_sum += int(line//3)-2

print("Part 1: {}".format(part_1_sum))
## Part 2
for line in data:
    while line > 5:
        line = line//3 - 2
        part_2_sum += line

print("Part 2: {}".format(part_2_sum))



    


print("Advent Of Code - Day 2")

PUZZLEINPUT = open('input.txt').read().strip().split(',')
data = [int(i) for i in PUZZLEINPUT]


for x in range(0, len(data), 4):
    x1, x2, x3 = data[x + 1], data[x + 2], data[x + 3]

    if data[x] == 1:
        data[x3] = data[x1]+data[x2]
    elif data[x] == 2:
        data[x3] = data[x1]*data[x2]
    elif data[x] == 99:
        break

print(data[0])
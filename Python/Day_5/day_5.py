
print("Advent Of Code - Day 2")

PUZZLEINPUT = open('input.txt').read().strip().split(',')

ADD = 1
MULTIPLY = 2
INPUT = 3
OUTPUT = 4
HALT = 99

POS_MODE = 0
IMM_MODE = 1


data = [int(i) for i in PUZZLEINPUT]

#Create the 1202 program
data[1] = 12
data[2] = 2


def opcode_runner(index,mem):
    for x in range(0, len(mem)):
        opcode = data[x]

        print(opcode)

    # if opcode == ADD:
    #     data[destination] = data[x1]+data[x2]
    # elif opcode == 2:
    #     data[destination] = data[x1]*data[x2]
    # elif opcode == 99:
    #     ## Terminate if opcode 99 is found
    #     break

# print(f'Part 1: {data[0]}')
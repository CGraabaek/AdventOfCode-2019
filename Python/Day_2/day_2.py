
print("Advent Of Code - Day 2")

PUZZLEINPUT = open('input.txt').read().strip().split(',')
data = [int(i) for i in PUZZLEINPUT]
#Create the 1202 program
data[1] = 12
data[2] = 2

for x in range(0, len(data), 4):
    opcode = data[x]
    x1, x2, destination = data[x + 1], data[x + 2], data[x + 3]

    if opcode == 1:
        data[destination] = data[x1]+data[x2]
    elif opcode == 2:
        data[destination] = data[x1]*data[x2]
    elif opcode == 99:
        ## Terminate if opcode 99 is found
        break

print(f'Part 1: {data[0]}')

original_data = [int(i) for i in PUZZLEINPUT]

for noun in range(0,100):
    for verb in range(0,100):
        current_data = [int(i) for i in original_data]
        #Create the new 1202 program
        current_data[1] = noun
        current_data[2] = verb
        for pointer in range(0, len(current_data), 4):
            opcode = current_data[pointer]
            x1, x2, destination = current_data[pointer + 1], current_data[pointer + 2], current_data[pointer + 3]

            if opcode == 1:
                current_data[destination] = current_data[x1]+current_data[x2]
            elif opcode == 2:
                current_data[destination] = current_data[x1]*current_data[x2]
            elif opcode == 99:
                ## Terminate if opcode 99 is found
                break
        if current_data[0] == 19690720:
            print(f'Part 2: {100 * noun + verb}')
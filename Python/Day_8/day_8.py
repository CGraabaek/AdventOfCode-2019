
from collections import defaultdict

print("Advent Of Code - Day 8")

PUZZLEINPUT = open('input.txt', 'r').read().split("\n")
input   = [int(x) for x in PUZZLEINPUT[0]]
IM_HEIGHT = 6
IM_WIDTH = 25

IM_PIXELS = IM_HEIGHT*IM_WIDTH

def get_layers(image):
    layer_count = int(len(image)/IM_PIXELS)

    layers = []
    x = 0
    y = 150
    for i in range(0,layer_count):
        layer = []
    
        for j in range(x,y):
            layer.append(image[j])

        layers.append(layer)
        if(y < 15000):
            x += 150
            y += 150
    return layers

layers = get_layers(input)
zero_counts  = [pixels.count(0) for pixels in layers]
result_layer = zero_counts.index(min(zero_counts))
print(f'Part 1: {layers[result_layer].count(1)*layers[result_layer].count(2)}')

def print_image(layers):
    layer_count = len(layers)
    for y in range(0,IM_HEIGHT):
        for x in range(0,IM_WIDTH):
            pos = x + y * IM_WIDTH
            for lay in range(0,layer_count):
                if layers[lay][pos] == 2:
                    continue
                if layers[lay][pos] == 1:
                    print("#", end="")
                else:
                    print(" ", end="")
                break
        print()
print('Part 2:')
print_image(layers)
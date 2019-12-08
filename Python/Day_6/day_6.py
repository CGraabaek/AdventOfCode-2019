
print("Advent Of Code - Day 6")

PUZZLEINPUT = open('input.txt', 'r').read().split("\n")

def get_position(orbits, planet):
    position = 0
    while planet in orbits.keys():
        planet = orbits[planet]
        position += 1
    return position 

#Get all orbits
def get_orbits(input):
    orbit_dict = {}

    for line in input:
        planets = line.split(')')
        orbit_dict[planets[1]] = planets[0]
    
    return orbit_dict

#Get all planets? from the input
def get_planets(input):
    planets = set(planet for line in input for planet in line.split(')'))
    return planets


orbits = get_orbits(PUZZLEINPUT)
all_planets = get_planets(PUZZLEINPUT)

print(f'Part 1: {sum(get_position(orbits, k) for k in all_planets)}')

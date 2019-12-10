
print("Advent Of Code - Day 6")

PUZZLEINPUT = open('input.txt', 'r').read().split("\n")

def get_planet_position(orbits, planet):
    position = 0
    while planet in orbits.keys():
        planet = orbits[planet]
        position += 1
    return position 

def get_planets(orbits, positions, planet):
    planets = []
    
    while planet in orbits.keys():
        planet = orbits[planet]
        planets.append(planet)
        
    return planets

#Get all orbits
def generate_orbits(input):
    orbit_dict = {}

    for line in input:
        planets = line.split(')')
        orbit_dict[planets[1]] = planets[0]
    
    return orbit_dict

#Get all planets? from the input
def get_all_planets(input):
    planets = set(planet for line in input for planet in line.split(')'))
    return planets

def get_all_positions(all_planets, orbits):
    positions = {}
    
    for planet in all_planets:
        positions[planet] = get_planet_position(orbits, planet)
    
    return positions


orbits = generate_orbits(PUZZLEINPUT)
all_planets = get_all_planets(PUZZLEINPUT)
all_positions = get_all_positions(all_planets,orbits)


san = get_planets(orbits, all_positions, "SAN")
you = get_planets(orbits, all_positions, "YOU")

print(san)

print(f'Part 1: {sum(get_planet_position(orbits, k) for k in all_planets)}')

# create the planets.txt
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
with open('planets.txt', 'w', encoding='utf-8') as file:
    for planet in planets:
        file.write(planet + '\n')

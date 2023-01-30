
"""
instantiate initial ants 

for time step
    
    for cell in pheromone map
        pheromones evaporate

    vvv THIS IS DONE
    for each ant (move loop)
        ant move algorithm
            if near trail
                check fidelity -> join or not join trail
            if on trail
                check fidelity -> stay on or leave trail
            if not on trail
                calculate probability of direction change
                rotate (if applicable) and step forward
    ^^^

    for each ant (pheromone loop)
        drop pheromone on pheromone map

    if time step % Rspawn == 0
        spawn new ant 
"""

from numpy import *
from ant import *
import matplotlib.pyplot as plt

# World  parameters and creation; world_map contains pheromone values.
world_width = 20
world_height = 20
spawn_point = (int(world_width/2), int(world_height/2))
spawn_rate = 2
world_map = []

for _ in range(0, world_height):
    world_map.append(zeros(world_width))

# Set up map plot
plt.axis([0, world_width, 0, world_height])

# Model parameters (x_pos, y_pos, fidelity, kernel)
fidelity = 0.8
kernel = [0.50, 0.25, 0.15, 0.085, 0.015]
max_concentration = 1.0
deposit_rate = 0.2  # Concentration for each ant to add each time step
evap_rate = 0.1   # Concentration to disappear each time step
time_steps = 200

if sum(kernel) != 1.0:  # Sanity check the kernel
    raise ValueError('Kernel values do not sum to 1.0.')

# EVAPORATE function
def evaporate(world_map):
    for r in range(0, len(world_map)):
        for c in range(0, len(world_map[r])):
            world_map[r][c] = world_map[r][c] - evap_rate
            value = world_map[r][c]
            if value <= 0:
                world_map[r][c] = 0.0
            elif value >= max_concentration:
                world_map[r][c] = max_concentration
    return world_map



# MAIN CODE BLOCK:

# Instantiate first ant object
ants = []
ants.append(Ant(spawn_point[0], spawn_point[1], fidelity, kernel))

# Conduct main loop
for t in range(0, time_steps):
    
    print("Time step " + str(t))
    for row in world_map:
        print(row)
    
    # Evaporate pheromones on the worldmap
    world_map = evaporate(world_map)
    # Run the move algorithm for each ant that exists
    for ant in ants:
        if ant.x >= 1 and ant.x <= world_width-2 and ant.y >= 1 and ant.y <= world_height-2:
            ant.move(world_map)
        else:
            ants.remove(ant)
        
    # Drop pheromones, ignoring ants that move out of the world
    for ant in ants:
        if ant.x >= 0 and ant.x <= world_width and ant.y >= 0 and ant.y <= world_height:
            world_map[ant.x][ant.y] = world_map[ant.x][ant.y] + deposit_rate
    # Respawn ant if 
    if t % spawn_rate == 0:
        ants.append(Ant(spawn_point[0], spawn_point[1], fidelity, kernel))
    
    plt.imshow(world_map, cmap="binary", interpolation="nearest")
    plt.pause(0.5)

plt.show()

    


from numpy import *
from ant import *
import matplotlib.pyplot as plt

# World  parameters and creation; world_map contains pheromone values.
world_size = 20
spawn_point = (10, 8)
world_map = []

for _ in range(0, world_size):
    world_map.append(zeros(world_size))
for i in range(0, world_size):
    world_map[i][i] = 0.25
    world_map[world_size-i-1][world_size-i-1] = 0.5

# Set up map plot
plt.axis([0, world_size, 0, world_size])

# Model parameters (x_pos, y_pos, fidelity, kernel)
fidelity = 0.9
kernel = [0.75, 0.2, 0.025, 0.025, 0.0]
max_concentration = 1.0
deposit_rate = 0.1  # Concentration for each ant to add each time step
time_steps = 10

if sum(kernel) != 1.0:  # Sanity check the kernel
    raise ValueError('Kernel values do not sum to 1.0.')

# MAIN CODE BLOCK:

# Instantiate first ant object
ant = Ant(spawn_point[0], spawn_point[1], fidelity, kernel)
ant.trail = True
ant.heading = 'S'

# Conduct main loop
for t in range(0, time_steps):
    
    print("Time step " + str(t) + ", Ant mode " + str(ant.trail))
    plt.imshow(world_map, cmap="binary", interpolation="nearest")
    point = plt.scatter(ant.y,ant.x,color='r')
    plt.pause(0.5)
    point.remove()


    # Run the move algorithm for each ant that exists
    if ant.x >= 1 and ant.x <= world_size-2 and ant.y >= 1 and ant.y <= world_size-2:
        ant.move(world_map)
        print(ant.x, ant.y)
        
    # Drop pheromones, ignoring ants that move out of the world
    if ant.x >= 0 and ant.x <= world_size and ant.y >= 0 and ant.y <= world_size:
        world_map[ant.x][ant.y] = world_map[ant.x][ant.y] + deposit_rate
    
    

plt.show()

    
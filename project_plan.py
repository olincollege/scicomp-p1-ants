
"""
---------------------------
Project 1 -- Ants
Braden & Tigey
---------------------------
Initial simplification: 

To reduce the number of variables we're dealing with we have opted to ignore
the "rise in phi as C increases to C_sat" which appears to enable a nonlinear
rise in following probability (phi) as the concentration (C) of a pheromone
increases towards a maximum value (C_sat).

---------------------------
General code structure:

Control variables:
 - World width and height (NxM)
 - Time (t)
 - Rate of pheromone deposition per time step (tau)
 - Probability per step of an ant remaining on a trail of concentration C (phi)
 - Minimum probability of remaining on trail (phi_min)
 - Ant pheromone saturation concentration (C_sat)
 - Spawn point coordinate (x,y)
 - Rate of new ant spawning (Rspawn)

Spawn ant function:
 - Instantiate new ant at spawn point

Pheromone map:
 - NxM array of cells containing a pheromone concentration (C)

Ant class:
 - Position (x, y)
 - Orientation (theta)
 - Mode (exploratory or trail-following)
 - Method for pulling data from map and making a decision for where to move next
 - Method for depositing pheromones on the map

---------------------------
Flow of computational model:

instantiate initial ants 

for time step
    
    for cell in pheromone map
        pheromones evaporate

    for each ant (move loop)
        ant move algorithm
            if near trail
                check fidelity -> join or not join trail
            if on trail
                check fidelity -> stay on or leave trail
            if not on trail
                calculate probability of direction change
                rotate (if applicable) and step forward

    for each ant (pheromone loop)
        drop pheromone on pheromone map

    if time step % Rspawn == 0
        spawn new ant 

---------------------------
Project timeline:

We plan on writing the majority of the code synchronously during class.  This will
need to vary as warranted by Braden's travel and Tigey's shifting course schedule.

Day 2 (1/26) - Build ant class and instantiator, build pheromone map, 
               formulate method of fidelity checking (synchronous work).
Day 3 (1/30) - Braden off campus, Tigey may drop out.  Asynchronously implement 
               fidelity checking algorithm if both available, Braden does otherwise.
Day 4 (2/02) - Test on small maps, tune control parameters, scale to larger maps.
Day 5 (2/06) - Code review, draft presentation.
Day 6 (2/09) - Presentation.

---------------------------
Benchmark:

Given Braden's travel and Tigey's uncertainty about whether he will remain in the 
class, we would like to create maps that resemble those in the paper.  The similarity 
between thebehavior of our model and theirs can be validated by skewing our control 
parameters in a similar way to how the authors did to verify whether the published 
maps  vary in a similar way to our own.  Because the authors reported specific 
parameter values for each of their maps, we can tune our parameters in a similar way.

---------------------------
Computing skill of focus (Braden):

Since coming back to Olin post-mission, I've made a concerted effort to revamp my math
and physics skills, but programming has been the one area I haven't really been able to
revisit yet.  As a result I'm feeling rusty at my programming, so I'd like to take this 
opportunity to practice combining object oriented programming with external data structures.
I've done projects where I've utilized lists of objects before, but I haven't done so at
the same scale as will be done here.  I'm particularly intersted in fusing lists of ant 
objects with the data structure for a map.

Looking ahead to the self project, I'm potentially interested in a particle-in-cell style
Hall thruster plume model.  In order to be able to do this, I need to be able to rapidly 
create pandas datastructures and think in gridspaces, two skills I think this project could
help me strengthen.

"""

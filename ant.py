
"""
---------------------------
Project 1 -- Ants
Braden & Tigey
---------------------------
Simplifications: 

1. Ants have only one behaviorial mode; they all follow the same rules and
there's no distinction between exploratory and trail-following ants.  

2. To reduce the number of variables we're dealing with we have opted to 
ignore the "rise in phi as C increases to C_sat" which appears to enable a
nonlinear rise in following probability (phi) as the concentration (C) of
a pheromone increases towards a maximum value (C_sat).  We've also opted to
ignore the B_n variable, which represents the probability that an exploratory 
ant turns 45 degrees.  We did this because we're not making a distinction

---------------------------
Flow of goal model:

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

    spawn new ant 

---------------------------
Project timeline:

Day 2 (1/26) - Build ant class, build pheromone map, formulate method of fidelity checking.
Day 3 (1/30) - Braden off campus. Implement fidelity checking algorithm.
Day 4 (2/02) - Test on 4x4 maps, tune control parameters, scale to larger maps.
Day 5 (2/06) - Code review, draft presentation.
Day 6 (2/09) - Presentation.

---------------------------
Benchmark:

Given Braden's travel and Tigey's uncertainty about whether he will remain in the class we
would like to create maps that resemble those in the paper.  The similarity between the
behavior of our model and theirs can be validated by modifying the same parameters the 
authors did to verify whether the published maps vary in a similar way to our own.  Because
the authors gave specific parameter values for each of their maps, we can tune our
parameters in a similar way.

---------------------------
Computing skill of focus:

---------------------------
General code structure:

Global variables:
 - World width and height (NxM)
 - Time (t)
 - Rate of pheromone deposition per time step (tau)
 - Probability per iteration of an ant remaining on a trail of concentration C (phi)
 - Minimum probability of remaining on trail (phi_min)
 - Ant pheromone saturation concentration (C_sat)

Pheromone map:
 - NxM array of cells containing a pheromone concentration (C)

Ant class:
 - Position (x, y)
 - Orientation (theta)
 - Mode (exploratory or trail-following)






"""

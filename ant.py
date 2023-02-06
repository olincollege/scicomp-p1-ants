
from numpy import *

class Ant:
    """
    - Position (x, y)
    - Orientation (theta)
    - Mode (exploratory or trail-following) -> implmeneted as Boolean 'trail'
    - Method for pulling data from map and making a decision for where to move next
    - Method for depositing pheromones on the map 
    """

    def __init__(self, x_pos, y_pos, fidelity, kernel):
        self.orientations = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
        self.x = x_pos
        self.y = y_pos
        self.heading = random.choice(self.orientations)
        self.trail = random.choice([True, False])
        self.fidelity = fidelity    # Decimal value from 0 to 1
        self.kernel = kernel        # 5 element list of decimals that add to 1
    
    """
    GET SURROUNDINGS: Retrieves values of pheromone levels surrounding my location
     - Takes 2D array worldmap as input.  Values of cells are pheromone levels.
    """
    def get_surroundings(self, worldmap):
        surroundings =  []
        # For each surrounding square
        for orientation in self.orientations:
            # Retrieve current coordinate
            coordinate_x = self.x
            coordinate_y = self.y
            # Retrieve surrounding square coordinate
            for char in orientation:
                # Directionality here matches 2D array with top row index 0
                if char == 'N' : coordinate_y -= 1
                if char == 'S' : coordinate_y += 1
                if char == 'E' : coordinate_x += 1
                if char == 'W' : coordinate_x -= 1
            # Retrieve pheromone value at relevant coordinate
            surroundings.append(worldmap[coordinate_x][coordinate_y])
        # Returns clockwise list starting at north
        return surroundings

    """
    REORIENT: Reorients a globally oriented surrounding list to our present heading
     - Takes 1D array surroundings as input.  Values of cells are pheromone levels.
    """
    def reorient(self, surroundings):
        offset = self.orientations.index(self.heading)
        return surroundings[offset:] + surroundings[:offset]

    """
    SHIFT POSITION: Updates my coordinates given my current heading
    """
    def shift_position(self):
        for char in self.heading:
            if char == 'N' : self.y -= 1
            if char == 'S' : self.y += 1
            if char == 'E' : self.x += 1
            if char == 'W' : self.x -= 1
        return None

    """
    EXPLORE MOVE: Pick a random heading (based on kernel) and move there
    """
    def explore_move(self):
        # pick a random heading based on the kernel
        new_heading_index = random.choice(arange(0, 5, 1), p=self.kernel) * random.choice([-1,1])
        self.heading = self.reorient(self.orientations)[new_heading_index]
        # move forward with that new heading
        self.shift_position()

    """
    MOVE: Executes the decision algorithm and decides where to go.
     - Takes 2D array worldmap as input.  Values of cells are pheromone levels.
    """
    def move(self, worldmap):
        
        # Retrieve the surroundings and reorient to match my heading
        surroundings = self.reorient(self.get_surroundings(worldmap))
        # Throw out the values of the square we just came from
        #surroundings.pop(4)
        # Throw out the values of all three squares behind me
        for _ in range(0,3):
            surroundings.pop(3)

        # if all surrounding squares are zero, I switch to explore mode
        if sum(surroundings) == 0:
            self.trail = False
        # otherwise I'll use the fidelity to decide whether to switch modes
        else:
            # if I lose the coin toss, switch modes
            if random.random() > self.fidelity:
                self.trail = not self.trail
            # otherwise leave my mode alone

        # if I'm in explore mode let's move randomly via the kernel
        if not self.trail:
            self.explore_move()

        # otherwise I'm in trail mode
        else:
            self.trail = True
            # if the highest concentration is straight ahead and only appears once,
            if (max(surroundings) == surroundings[0]) and (surroundings.count(max(surroundings)) == 1):
                # maintain the current heading and move forward
                self.shift_position()
            
            # if there are multiple maximum values, let's explore
            elif surroundings.count(max(surroundings)) > 1:
                self.explore_move()

            # otherwise let's follow the strongest pheromone trail
            else:
                # get the index of the strongest heading
                strongest = surroundings.index(max(surroundings))
                # use that index to set our new heading in that direction
                self.heading = self.reorient(self.orientations)[strongest]
                # go move there!
                self.shift_position()

    """
    ALTERNATE MOVE: Executes the decision algorithm and decides where to go.
     - Takes 2D array worldmap as input.  Values of cells are pheromone levels.
    """
    def alt_move(self, worldmap):
        
        # Retrieve the surroundings and reorient to match my heading
        surroundings = self.reorient(self.get_surroundings(worldmap))
        # Throw out the values of the square we just came from
        #surroundings.pop(4)
        # Throw out the values of all three squares behind me
        for _ in range(0,3):
            surroundings.pop(3)

        # if all surrounding squares are zero, I switch to explore mode
        if sum(surroundings) == 0:
            self.trail = False
        # otherwise I'll use the fidelity to decide whether to switch modes
        else:
            # if I lose the coin toss, switch modes
            if random.random() > self.fidelity:
                self.trail = not self.trail
            # otherwise leave my mode alone

        # if I'm in explore mode let's move randomly via the kernel
        if not self.trail:
            self.explore_move()

        # otherwise I'm in trail mode
        else:
            self.trail = True
            # if the highest concentration is straight ahead and only appears once,
            if (max(surroundings) == surroundings[0]) and (surroundings.count(max(surroundings)) == 1):
                # maintain the current heading and move forward
                self.shift_position()

            # if there are multiple strongest values, let's follow the strongest one
            elif surroundings.count(max(surroundings)) > 1:
                # get the index of the strongest heading
                strongest = surroundings.index(max(surroundings))
                # use that index to set our new heading in that direction
                self.heading = self.reorient(self.orientations)[strongest]
                # go move there!
                self.shift_position()

            # only as a last resort, let's explore
            else:
                self.explore_move()
    
    """
    DEBUG MOVE: Walk straight ahead
    """
    def debug_move(self):
        self.heading = self.reorient(self.orientations)[0]
        # move forward with that new heading
        self.shift_position()
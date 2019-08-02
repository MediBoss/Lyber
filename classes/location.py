from typing import Dict

class Location(object):
    
    def __init__(self, name: str):
        """ Initializes a new location object with a name"""

        self.__name = name
        self.neighbors: [Location, int] = {}

    def __eq__(self, location: Location):
        ''' Overrides the == operator and defines the equality between two location '''
        return self.__name == location.name


    # Getters & Setters
    def get_name(self) -> str:
        return self.__name

    def set_name(self, new_name: str) -> str:
        self.__name = new_name

    def add_neighbor(self, location: Location, time=0):
        """
            Connects one location to another with the time it takes to travel between them.
            Time & Space Complexity: O(1) | O(1)
        """
        if location not in self.neighbors:
            self.neighbors[location] = time
            return True
        return False

    def get_weighted_neighbors(self, location: Location):
        
        return [neighbor for neighbor,weight in self.neighbors.items()]

    

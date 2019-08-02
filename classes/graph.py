from typing import Dict, List, Tuple
from location import Location

class Graph:
    def __init__(self):
        """Initialize a graph object with an empty dictionary, number of edges and vertices"""
        self.graph: [str, Location] = {}
        self.edges = 0
        self.vertices = 0

    def __iter__(self):
        """Iterate over the vertex objects in the graph, to use sytax: for v in g"""
        return iter(self.graph.values())

    def add_location(self, key: str):
        """Add a new vertex object to the graph with the given key and return the vertex.
            Time & Space complexity : O(1) | O(1)
        """
        vertex = Vertex(key)
        self.vertices += 1
        self.graph[key] = vertex

        return vertex

    def add_many_locations(self, locations: List[Location]):
        
        for location in locations:
            self.add_location(location)


    def get_vertex(self, key):
        """Return the vertex if it exists
            Time & Space Complexity : O(1) | O(1)
        """

        vertex = None
        try: 
           vertex = self.graph[key]
        except KeyError:
            raise ValueError("Vertex with key {} not in Graph".format(key))

        return vertex


    def add_edge(self, key1, key2, weight=0):
        """add an edge from vertex with key `key1` to vertex with key `key2` with a cost."""

    
        if key1 not in self.graph and key2 not in self.graph:
            raise ValueError("Both Vertex of keys {} and {} not in Graph".format(key1, key2))
        elif key1 not in self.graph or key2 not in self.graph:
            raise ValueError("Either Vertex of keys {} and {} not in Graph".format(key1, key2))

        elif key1 == key2:
            raise ValueError("Vertex {} can't be its own neighbor".format(key1))
        else:
            # Get the two neighbor verteces
            vertex_one = self.graph[key1]
            vertex_two = self.graph[key2]

            # Code idea from Vicenzo : https://github.com/C3NZ/CS22/blob/master/challenges/graph.py#L77
            added_from = vertex_one.add_neighbor(vertex_two, weight)
            added_to = vertex_two.add_neighbor(vertex_one, weight)

            if added_from and added_to:
                self.edges += 1

    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.graph.keys()
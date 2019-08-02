# Lyber

CS 2.2 Custom Final project : Modeling and solving Uber/Lyft group's ride-sharing algorithm using Graph Theory.

# Overview
In a ride-sharing vehicle with n people going to n destination starting at point x,  find: 
* The shortest itinerary  to drop off everyone at their destination with a time-frame per person.
* The group of people who are in the same neighborhood.
* The distance (minutes) between two person's location in the graph.


# Modeling
Inside the <b>undirected graph</b>, each location would be a vertex, weights on the edge represents the time in minutes.

# Classes
- Person
    - name: string
    - origin: Location
    - destination: Location
    - time: Date

- Location(vertex)
    - id
    - neighbors

- Graph
    - network
    - edges 
    - vertices
class Person(object):
    
    def __init__(self, name, origin, destination, time=None):
        
        self.name = name
        self.origin = origin
        self.destination = destination
        self.time = time

    
    def increment_time(self, additional_time):
        self.time += additional_time

    def decrement_time(self, by_time):
        self.time -= by_time
class Animal(object):
    
    def __init__(self, name=None, species=None, next=None):
        self.name = name
        self.species = species
        self.next = next
        self.tracker_counter = 0
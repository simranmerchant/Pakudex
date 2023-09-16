from pakuri import Pakuri
# import class from file

class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity # initial value is 20
        self.pakuris = [] # store a list of pakuri objects
        self.size = 0 # keep track of the # of concrete pakuri objects
        self.names = []

    # getters
    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        # self.names appended in add_pakuri, return here
        if len(self.names) == 0:
            return None
        return self.names

    def get_stats(self, species):
        res = []
        for pakuri in self.pakuris:
            if pakuri.species == species:
                res.extend([pakuri.attack, pakuri.defense, pakuri.speed])
        # return None if species not in pakuri.species
        if len(res) == 0:
            return None
        else:
            return res


    def sort_pakuri(self):
        # sort current list and update
        self.names.sort()
        return self.names

    # species vs. pakuri object
    def add_pakuri(self, species):
        # catch duplicates
        if species in self.names:
            return False
        else:
        # add a new pakuri object into the list
            self.pakuris.append(Pakuri(species))
        # increment self.size
            self.size += 1
            self.names.append(species) # create list
            return True


    def evolve_species(self, species):
        # evolve if there is a pakuri and return true, otherwise return false
        for pakuri in self.pakuris:
            if pakuri.species == species:
                pakuri.evolve()
                return True
        return False


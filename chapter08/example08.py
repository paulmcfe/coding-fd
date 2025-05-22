class Pet:

    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def print_info(self):
        print(f"{self.name} is a {self.age}-year-old {self.species}.")

chase = Pet("Chase", "dog", 3)
whiskers = Pet("Whiskers", "cat", 1)
hammy = Pet("Hammy", "hamster", 2)

chase.print_info()
whiskers.print_info()
hammy.print_info()
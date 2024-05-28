class Dog:
    approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]

    def __init__(self, name="Mutt", breed="Mutt"):
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be a string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed

    def set_breed(self, value):
        if value in self.approved_breeds:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)

from abc import ABC
from classes.Animal import Animal

class PackAnimal(Animal, ABC):
    def __init__(self, name, type_animal, birth_day, commands):
        super().__init__(name, type_animal, birth_day)
        self.commands = commands

class Camel(PackAnimal):
    def __init__(self, name, type_animal, birth_day, commands):
        super().__init__(name, type_animal, birth_day, commands)

class Horse(PackAnimal):
    def __init__(self, name, type_animal, birth_day, commands):
        super().__init__(name, type_animal, birth_day, commands)

class Donkey(PackAnimal):
    def __init__(self, name, type_animal, birth_day, commands):
        super().__init__(name, type_animal, birth_day, commands)
from abc import ABC
from classes.Animal import Animal

class PackAnimal(Animal, ABC):
    def __init__(self, name, type_animal, birth_day):
        super().__init__(name, type_animal, birth_day)

class Camel(PackAnimal):
    def __init__(self, name, type_animal, birth_day):
        super().__init__(name, type_animal, birth_day)

class Horse(PackAnimal):
    def __init__(self, name, type_animal, birth_day):
        super().__init__(name, type_animal, birth_day)

class Donkey(PackAnimal):
    def __init__(self, name, type_animal, birth_day):
        super().__init__(name, type_animal, birth_day)
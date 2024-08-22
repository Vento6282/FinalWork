from abc import ABC
from classes.Animal import Animal

class Pet(Animal, ABC):
    def __init__(self, name, type_animal, birth_day, commands):
        super().__init__(name, type_animal, birth_day)
        self.commands = commands
    def get_commands(self):
        return self._commands

class Cat(Pet):
    def __init__(self, name, type_animal, birth_day, commands):
        super().__init__(name, type_animal, birth_day, commands)

class Hamster(Pet):
    def __init__(self, name, type_animal, birth_day, commands):
        super().__init__(name, type_animal, birth_day, commands)

class Dog(Pet):
    def __init__(self, name, type_animal, birth_day, commands):
        super().__init__(name, type_animal, birth_day, commands)
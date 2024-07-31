from abc import ABC
from classes.Animal import Animal

class Pet(Animal, ABC):
    def __init__(self, name, type_animal, birth_day):
        super().__init__(name, type_animal, birth_day)

class Cat(Pet):
    def __init__(self, name, type_animal, birth_day):
        super().__init__(name, type_animal, birth_day)

class Hamster(Pet):
    def __init__(self, name, type_animal, birth_day):
        super().__init__(name, type_animal, birth_day)

class Dog(Pet):
    def __init__(self, name, type_animal, birth_day):
        super().__init__(name, type_animal, birth_day)
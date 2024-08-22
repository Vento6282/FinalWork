from abc import ABC

class Animal(ABC):
    
    def __init__(self, name, type_animal, birth_day):
        self._name = name
        self._type = type_animal
        self._birth_day = birth_day

    def get_name(self):
        return self._name
    
    def get_type(self):
        return self._type
    
    def get_birth_day(self):
        return self._birth_day
    
    def show_animal(self):
        return self.get_type().lower() + ' ' + self.get_name() + ' ' + self.get_birth_day()
    
    def get_parent_type(self):
        return type(self).mro()[1].__name__   

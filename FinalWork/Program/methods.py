from datetime import datetime

from classes.Pet import *
from classes.PackAnimal import *
from dictionaries.dict import animal_types
from dictionaries.dict import animal_classes

def write_to_file(animal):
    with open('FinalWork\Program\List of animals.csv', 'a', encoding='utf-8') as file:
        file.write(animal)

def check_animal_name(animal_name):
    if len(animal_name) > 0 and len(animal_name.strip()) == 0:
        print('Имя не может состоять только из пробелов!')
        return False
    if len(animal_name) == 0:
        print('Слишком короткое имя!')
        return False
    if animal_name.find(';') != -1:
        print('В имени не может быть символа ";"!')
        return False       
    else:
        return True

def check_date(birth_day):
    try:
        date_birth_day = datetime.strptime(birth_day, '%Y-%m-%d').date()
        cur_date = datetime.now().date()
        if date_birth_day > cur_date:
            print('Дата рождения не может быть позже текущей даты!')
            return False
        return True
    except ValueError:
        print('Введён неверный формат даты!')
        return False

def check_duplicate_animal(animal_type, animal_name, animal_birth_day):
    with open('FinalWork\Program\List of animals.csv', 'r', encoding='UTF-8') as file:
        animal_list = file.read().rstrip().split('\n')
        if animal_list[0] != '':
            for animal_of_list in animal_list:
                animal = animal_of_list.rstrip().split(';')
                if animal_name == animal[1] and animal_type == animal[2] and animal_birth_day == animal[3]:
                    print(f'В базе уже есть {animal[1].lower()} с именем {animal[2]} и датой рождения {animal[3]}')
                    return False
        else:
            return True
    return True

def extract_animal_commands(animal_commands):
    print('-' * 60)
    commands_list = animal_commands.strip().split(',')
    commands = set()
    for command in commands_list:
        if len(command.strip())> 0:
            commands.add(command.strip()) 
    commands_str = ','.join(commands)

    return commands_str

def create_animal(animal_name, animal_type, animal_birth_day, commands):
    match animal_type:
        case 'Лошадь':   
            new_animal = Horse(animal_name, animal_type, animal_birth_day, commands)
        case 'Кот':   
            new_animal = Cat(animal_name, animal_type, animal_birth_day, commands)
        case 'Осёл':   
            new_animal = Donkey(animal_name, animal_type, animal_birth_day, commands)
        case 'Собака':   
            new_animal = Dog(animal_name, animal_type, animal_birth_day, commands)
        case 'Верблюд':   
            new_animal = Camel(animal_name, animal_type, animal_birth_day, commands)
        case 'Хомяк':   
            new_animal = Hamster(animal_name, animal_type, animal_birth_day, commands)
        
    write_to_file(f'{animal_classes[new_animal.get_parent_type()]};{new_animal.get_type()};{new_animal.get_name()};{new_animal.get_birth_day()};{new_animal.commands}\n')
from datetime import datetime

from classes.Pet import *
from classes.PackAnimal import *
from dictionaries.dict import animal_types
from dictionaries.dict import animal_classes

def write_to_file(animal):
    with open('FinalWork\Program\List of animals.csv', 'a', encoding='utf-8') as file:
        file.write(animal)

def request_animal_name():
    print('-' * 60)
    animal_name = input('Введите имя животного: ')
    while not check_animal_name(animal_name):
        print('-' * 60)
        animal_name = input('Введите имя животного: ')
    return animal_name

def request_birth_day():
    print('-' * 60)
    animal_birth_day = input('Введите дату рождения животного в формате 2024-07-15: ')
    while not check_date(animal_birth_day):
        print('-' * 60)
        animal_birth_day = input('Введите дату рождения животного в формате 2024-07-15: ')
    return animal_birth_day

def check_double_animal(animal_type, animal_name, animal_birth_day):
    with open('FinalWork\Program\List of animals.csv', 'r', encoding='UTF-8') as file:
        animal_list = file.read().rstrip().split('\n')
        for animal_of_list in animal_list:
            animal = animal_of_list.rstrip().split(',')
            # print(animal_name+'='+animal[1]+'   '+animal_type+'='+animal[2]+'   '+animal_birth_day+'='+animal[3])
            if animal_name == animal[1] and animal_type == animal[2] and animal_birth_day == animal[3]:
                print(f'В базе уже есть {animal[1].lower()} с именем {animal[2]} и датой рождения {animal[3]}')
                return False
    return True

def check_animal_name(animal_name):
    if len(animal_name) == 0:
        print('Слишком короткое имя!')
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
    
def create_animal(animal_name, animal_type, animal_birth_day):
    if check_double_animal(animal_name, animal_type, animal_birth_day):
        match animal_type:
            case 'Лошадь':   
                new_animal = Horse(animal_name, animal_type, animal_birth_day)
            case 'Кот':   
                new_animal = Cat(animal_name, animal_type, animal_birth_day)
            case 'Осёл':   
                new_animal = Donkey(animal_name, animal_type, animal_birth_day)
            case 'Собака':   
                new_animal = Dog(animal_name, animal_type, animal_birth_day)
            case 'Верблюд':   
                new_animal = Camel(animal_name, animal_type, animal_birth_day)
            case 'Хомяк':   
                new_animal = Hamster(animal_name, animal_type, animal_birth_day)
        
        # print(animal_classes[new_animal.get_parent_type()] + ',' + animal_type + ',' + animal_name + ',' + animal_birth_day)

        print('-' * 60)
        question = f'{animal_classes[new_animal.get_parent_type()].lower()} {animal_type.lower()} с именем {animal_name} и датой рождения {animal_birth_day}'
        # question = f'Добавить {animal_classes[new_animal.get_parent_type()].lower()} {animal_type.lower()} с именем {animal_name} и датой рождения {animal_birth_day} в реестр? \nВведите "yes" или "no": '
        
        answer = input(f'Добавить {question}, "yes" или "no"? ')

        while answer not in ('yes', 'no'):
            if answer == 'yes':
                write_to_file(animal_classes[new_animal.get_parent_type()] + ',' + animal_type + ',' + animal_name + ',' + animal_birth_day + '\n')
                print('Животное добавлено!')
            elif answer == 'no':
                print('Добавление животного отменено!')
            else:
                print('Введён некорректный ответ!')
                print('-' * 60)
                answer = input(f'Добавить {question}?')
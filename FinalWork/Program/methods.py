from datetime import datetime
from classes.Pet import *
from classes.PackAnimal import *
from dictionaries.dict import animal_types
from dictionaries.dict import animal_classes

# добавление записи в файл
def write_to_file(animal):
    with open('FinalWork\Program\List of animals.csv', 'a', encoding='utf-8') as file:
        file.write(animal)
        file.write('\n')

# проверка корректности имени
def is_name(animal_name):
    s = '.:;!_*+()/#%&'
    if len(animal_name) > 0 and len(animal_name.strip()) == 0:
        print('Имя не может состоять только из пробелов!')
        return False
    elif len(animal_name) == 0:
        print('Слишком короткое имя!')
        return False    
    for char in s:
        if char in animal_name:
            print (f'Введён недопустимый символ - {char}!')
            return False
    return True

# проверка, что дата корректного формата
def is_date(birth_day):
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

# проверка, есть ли дубликаты записи по типу, имени и дате рождения
def is_duplicate_animal(animal_type, animal_name, animal_birth_day):
    with open('FinalWork\Program\List of animals.csv', 'r', encoding='UTF-8') as file:
        animal_list = file.read().rstrip().split('\n')
        if animal_list[0] != '':
            for animal_of_list in animal_list:
                animal = animal_of_list.rstrip().split(';')
                if animal_type.lower() == animal[1].lower() and animal_name.lower() == animal[2].lower() and str(animal_birth_day) == str(animal[3]):
                    print(f'В базе уже есть {animal[1].lower()} с именем {animal[2]} и датой рождения {animal[3][:-9]}')
                    return True
    return False

# проверка строки с командами
def is_correct_commands(commands):
    s = '.:;!_*+()/#%&'
    for char in s:
        if char in commands:
            print (f'Введён недопустимый символ - {char}!')
            return False
    return True

# преобразорвание строки в формат, необходимый для поля с командами
def extract_animal_commands(animal_commands):
    commands_list = animal_commands.strip().split(',')
    commands = set()
    for command in commands_list:
        if len(command.strip())> 0:
            commands.add(command.strip()) 
    commands_str = ','.join(commands)
    return commands_str.lower()

# создание объекта необходимого класса
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
    return new_animal

# проверка, есть ли в таблице хоть одна запись
def is_list_empty():
    with open('FinalWork\Program\List of animals.csv', 'r', encoding='UTF-8') as file:
        animal_list = file.read().strip().split('\n')
        if animal_list[0] == '':
            print('Реестр животных пуст!')
            return True
    return False

# определение размеров полей для отображения таблицы
def show_animal_sizes(show_type, show_animal, show_name, show_date, show_commands):   
    with open('FinalWork\Program\List of animals.csv', 'r', encoding='UTF-8') as file:
        animal_list = file.read().strip().split('\n') 
    size_type = len(show_type)
    size_animal = len(show_animal)
    size_name = len(show_name)
    size_date = len(show_date)
    size_commands = len(show_commands)
    for animal_str in animal_list:
        animal = animal_str.split(';')
        if len(animal[0]) > size_type:
            size_type = len(animal[0]) 
        if len(animal[1]) > size_animal:
            size_animal = len(animal[1]) 
        if len(animal[2]) > size_name:
            size_name = len(animal[2]) 
        if len(animal[3]) > size_date:
            size_date = len(animal[3]) 
        if len(animal[4]) > size_commands:
            size_commands = len(animal[4]) 
    return [size_type, size_animal, size_name, size_date, size_commands]

# поиск записи по имени
def search_name(animal_name):
    with open('FinalWork\Program\List of animals.csv', 'r', encoding='UTF-8') as file:
        animal_list = file.read().strip().split('\n') 
    result = []
    i = 0
    for animal_str in animal_list:
        animal = animal_str.split(';')
        if animal_name.lower() == animal[2].lower():
            result.append([len(result) + 1,animal[0], animal[1], animal[2], animal[3], animal[4], i])
        i = i + 1
    if len(result) == 0 and animal_name != '':
        print(f'Не найдено животное с именем {animal_name}')   
        return 0
    else:
        return result
    
# удаление записи из таблицы
def delete_animal(index):
    with open('FinalWork\Program\List of animals.csv', 'r', encoding='UTF-8') as file:
        animal_list = file.read().strip().split('\n')   
        animal_list.pop(index)
        with open('FinalWork\Program\List of animals.csv', 'w', encoding='utf-8') as file:
            file.write('\n'.join(animal_list))        
        with open('FinalWork\Program\List of animals.csv', 'a', encoding='utf-8') as file:
            file.write('\n')  
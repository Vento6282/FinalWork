from methods import *

from classes.Pet import *
from classes.PackAnimal import *

animals = {'1':['Рorse', 'Лошадь'], 
           '2':['Сamel', 'Верблюд'], 
           '3':['Вonkey', 'Осёл'],
           '4':['Сat', 'Кот'],
           '5':['Dog', 'Собака'],
           '6':['Hamster', 'Хомяк']}

animal_types = {'PackAnimal':'Вьючное животное',
                'Pet':'Домашнее животное'}

def menu_main():
    command = '-1'
    while command != '0':
        print('-' * 30)
        print('Главное меню. Возможные действия:\n'
            '1. Добавить новое животное\n'
            '2. Вывести всех животных\n'
            '3. Обучить животное новой команде\n'
            '4. Удалить животное из списка\n'
            '0. Выход из программы')
        
        command = input('Введите пункт меню: ')
        
        if (command not in ('1', '2', '3', '4', '0')):
            print('Пункта с таким номером нет!!!')

        match command:
            case '1':   
                menu_add_animal()
            case '2':    
                #show_animals()
                print(2)          
            case '3':   
                #to_teach_animal_to_commands()
                print(3)            
            case '4':   
                #remove_animal()
                print(4)
            case '0':   
                print('-' * 30)
                print('До новых встреч!')

def menu_add_animal():

    type_animal = '-1'
    while type_animal < '0' or int(type_animal) > len(animals):
        print('-' * 30)
        print('Выберите вид животного:')
        for key in animals:
            print(f"{key}. {animals[key][1]}")
        print('0. Выход в главное меню')
        type_animal = input('Введите пункт меню: ')
        if(type_animal == '0'):
            menu_main()
        if type_animal < '0' or int(type_animal) > len(animals):
            print('Пункта с таким номером нет!!!')
    
    name = input('Введите имя животного: ')

    birth_day = input('Введите дату рождения животного: ')

    match animals[type_animal][1]:
        case 'Лошадь':   
            new_animal = Horse(name, animals[type_animal][1], birth_day)
        case 'Кот':   
            new_animal = Cat(name, animals[type_animal][1], birth_day)
        case 'Осёл':   
            new_animal = Donkey(name, animals[type_animal][1], birth_day)
        case 'Собака':   
            new_animal = Dog(name, animals[type_animal][1], birth_day)
        case 'Верблюд':   
            new_animal = Camel(name, animals[type_animal][1], birth_day)
        case 'Хомяк':   
            new_animal = Hamster(name, animals[type_animal][1], birth_day)

    # print(animals[type_animal][1]) 

    # print(animal_types[new_animal.get_parent_type()])

    # print('Добавлено животное: ' + new_animal.show_animal())

    print(animal_types[new_animal.get_parent_type()] + ',' + animals[type_animal][1] + ',' + name + ',' + birth_day)
    write_to_file([animal_types[new_animal.get_parent_type()],animals[type_animal][1],name,birth_day])
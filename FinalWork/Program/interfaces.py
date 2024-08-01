from methods import *
from classes.Pet import *
from classes.PackAnimal import *

def menu_main():
    command = '-1'
    while command != '0':
        print('-' * 60)
        print('Главное меню:\n'
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
                print('-' * 60)
                print('До новых встреч!')
                print('-' * 60)

def menu_add_animal():

    animal_type = '-1'
    while animal_type < '0' or int(animal_type) > len(animal_types):
        print('-' * 30)
        print('Выберите вид животного:')
        for key in animal_types:
            print(f"{key}. {animal_types[key][1]}")
        print('0. В главное меню')
        animal_type = input('Введите пункт меню: ')
        if(animal_type == '0'):
            menu_main()
        if animal_type < '0' or int(animal_type) > len(animal_types):
            print('Пункта с таким номером нет!!!')
    
    animal_name = request_animal_name()

    animal_birth_day = request_birth_day()      

    if not check_double_animal(animal_name, animal_types[animal_type][1], animal_birth_day):
         menu_add_animal()

    # question = f'{animal_classes[new_animal.get_parent_type()].lower()} {animal_type.lower()} с именем {animal_name} и датой рождения {animal_birth_day}'

    

    # # question = f'Добавить {animal_classes[new_animal.get_parent_type()].lower()} {animal_type.lower()} с именем {animal_name} и датой рождения {animal_birth_day} в реестр? \nВведите "yes" или "no": '
        
    # answer = input(f'Добавить {question}, "yes" или "no"? ')

    # create_animal(animal_name, animal_types[animal_type][1], animal_birth_day)